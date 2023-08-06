# This file is part of the RIBFIND (https://gitlab.com/topf-lab/ribfind)
# Copyright (c) 2022 RIBFIND Developers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
"""Interactions"""
from typing import List
from ribfind.model import RNAHelix, RNAStrand, Helix, Sheet, Residue
from ribfind.graph import Graph
from ribfind.contact import ContactMap


class Interaction:
    """TODO"""

    def __init__(self, contacts):
        self.__contacts = contacts
        self._residues = {}

    def _get_asym_interaction(self, this, that) -> float:
        num_interactions = 0.0
        checker = self.__contacts.checker(self.get_modelled_residues(that))
        for residue in self.get_modelled_residues(this):
            if checker.in_contact(residue):
                num_interactions += 1.0

        if num_interactions == 0:
            return 0
        return num_interactions / float(len(self.get_modelled_residues(this)))

    def soft_interaction(self, this, that):
        """Compute a soft interaction strength, based on distances rather than cutoff"""
        max_strength = 0.0
        for this_residue in self.get_modelled_residues(this):
            for that_residue in self.get_modelled_residues(that):
                if this_residue != that_residue:
                    dist = self.__contacts.dist(this_residue, that_residue)
                    strength = dist**-2
                    max_strength = max(max_strength, strength)

        return max_strength

    def default_interaction(self, this_model, that_model) -> float:
        """TODO"""
        return max(
            self._get_asym_interaction(this_model, that_model),
            self._get_asym_interaction(that_model, this_model),
        )

    def get_modelled_residues(self, sse) -> List[Residue]:
        """Gets all residues which have centroids.

        This is necessary because SSEs are modelled as contigs with a start and end
        residue, however numbering is not always continuous.  There maybe residues
        numbers in the range that are not present."""
        res = self._residues.get(sse.model_id)
        if res is not None:
            return res
        res = [r for r in self.get_residues(sse) if self.__contacts.has_centroid(r)]
        self._residues[sse.model_id] = res
        return res

    def get_residues(self, sse) -> List[Residue]:
        """All interactions should implement this method.

        Return the residues in the SSE that should interact"""
        raise NotImplementedError("TODO")

    def calculate(self, this_sse, that_sse) -> float:
        """Interactions should over-ride this for more control"""
        return self.default_interaction(this_sse, that_sse)

    def pairs(self, models):
        """Returns pairs of models that may interact"""
        model_ids = {}
        pairs = set()

        mapper = ContactMap(self.__contacts)
        for model in models:
            model_ids[model.model_id] = model
            for res in self.get_modelled_residues(model):
                for neig in mapper.neighbours(res):
                    pairs.add((model.model_id, neig))
                mapper.map_residue(res, model.model_id)

        for this_model, that_model in pairs:
            this_model = model_ids[this_model]
            that_model = model_ids[that_model]
            yield (this_model, that_model)

    def graph(self, models) -> Graph:
        """Compute an interaction graph, where edges are interactions."""
        graph = Graph()

        for this_model, that_model in self.pairs(models):
            strength = self.calculate(this_model, that_model)
            if strength > 0:
                graph.add_edge(this_model, that_model, strength)
        return graph

    def soft_graph(self, models) -> Graph:
        """Compute an interaction graph, where edges are interactions."""
        graph = Graph()

        for this_model, that_model in self.pairs(models):
            strength = self.soft_interaction(this_model, that_model)
            if strength > 0:
                graph.add_edge(this_model, that_model, strength)
        return graph


class ProteinInteractions(Interaction):
    """The interaction rules for proteins.

    In general, interaction is defined as the fraction of residues within the
    'contact_dist' (default 6.5) of two SSEs.

    However, there are a couple of other rules:

    * Two helices which have a length ratio less than 'helix_ratio' do not
      interact. (default 0.4)

    * All residues in sheets are involved in interactions except those in
      strands with less than 'minimum_strand_length' residues. (default 4)

    * Helices with less than minimum_helix_length residues (default 4) do not interact.
    """

    def __init__(
        self,
        contacts,
        helix_ratio=0.4,
        minimum_strand_length=4,
        minimum_helix_length=4,
    ):
        super().__init__(contacts)
        self.helix_ratio = helix_ratio
        self.minimum_strand_length = minimum_strand_length
        self.minimum_helix_length = minimum_helix_length
        self.hh_interactions = 0
        self.mm_interactions = 0

    def get_residues(self, sse) -> List[Residue]:
        """Get the interacting residues in an SSE.  If the SSE is a sheet,
        excludes residues from strands less than 'minimum_strand_length'.

        If SSE is a helix, returns no residues if length is not greater or equal
        'minimum_helix_length'."""
        if isinstance(sse, Sheet):
            return [
                r
                for strand in sse.get_contigs()
                for r in strand.residues()
                if len(strand) >= self.minimum_strand_length
            ]
        if isinstance(sse, Helix):
            if len(sse) >= self.minimum_helix_length:
                return sse.residues()
            return []
        raise Exception("Don't have rule to get residues from type:", type(sse))

    def get_helix_interaction(self, this_helix, that_helix) -> float:
        """If the ratio between the helix lengths is below `helix_ratio`
        the helices do not interact.  Otherwise they use the default
        interaction method"""
        small = min(len(this_helix), len(that_helix))
        large = max(len(this_helix), len(that_helix))

        if (small / large) <= self.helix_ratio:
            return 0
        return self.default_interaction(this_helix, that_helix)

    def calculate(self, this_sse, that_sse) -> float:
        """Given two protein SSEs calculates their interaction"""
        if isinstance(this_sse, Helix) and isinstance(that_sse, Helix):
            return self.get_helix_interaction(this_sse, that_sse)
        return self.default_interaction(this_sse, that_sse)


class RNAInteractions(Interaction):
    """TODO"""

    def __init__(self, contacts, minimum_strand_length=4):
        super().__init__(contacts)
        self.minimum_strand_length = minimum_strand_length

    def get_residues(self, sse) -> List[Residue]:
        """Rules for interacting RNA SSEs.

        - If SSE is an RNA Strand, it must have at least 4 nucleic acids.
        - If SSE is an RNA Helix, any strand which satisfies the above rule
          is also involved in interaction calculations.
        """
        if isinstance(sse, RNAStrand):
            if len(sse) >= self.minimum_strand_length:
                return sse.residues()
            return []
        if isinstance(sse, RNAHelix):
            return [
                r for contig in sse.get_contigs() for r in self.get_residues(contig)
            ]
        raise Exception("Don't have rule to get residues from type:", type(sse))
