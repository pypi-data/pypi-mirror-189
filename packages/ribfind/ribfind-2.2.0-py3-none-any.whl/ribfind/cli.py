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
import argparse
import os
from Bio.PDB import PDBParser

import ribfind
from ribfind.dssp import DSSPContigReader
from ribfind.rnamlparse import parse_rna_model
from ribfind.interaction import ProteinInteractions, RNAInteractions
from ribfind.contact import make_protein_contacts, make_rna_contacts
from ribfind.cluster import get_solutions
from ribfind.writers import Writer


def write_files(model, graph_method, cutoff, writer):
    solutions = get_solutions(model, graph_method, dens_cutoff=cutoff, add_loops=True)
    writer.write(solutions)


def run(args):
    # Parse PDB file
    parser = PDBParser()
    structure = parser.get_structure("id", args.model)

    if args.output_dir:
        base_path = args.output_dir
    else:
        base_path, _ = os.path.splitext(os.path.basename(args.model))

    # Build mapping of contigs and SSEs from DSSP file.
    if args.dssp:
        dssp_reader = DSSPContigReader()
        protein_model = dssp_reader.parse_model(args.dssp)

        # Calculate contacts based on side chain centers
        contacts = make_protein_contacts(
            structure, dist_cutoff=args.protein_contact_distance
        )

        # Configure interaction rules
        interactions = ProteinInteractions(
            contacts,
            helix_ratio=args.protein_helix_ratio,
            minimum_strand_length=args.protein_minimum_strand_length,
        )

        writer = Writer(
            f"{base_path}/protein", args.model, args.protein_contact_distance
        )

        if args.soft_cutoff:
            graph_method = interactions.soft_graph
        else:
            graph_method = interactions.graph
        write_files(protein_model, graph_method, args.protein_dens_cutoff, writer)

    if args.rnaml:
        rna_model = parse_rna_model(args.rnaml, structure)
        rna_contacts = make_rna_contacts(
            structure, dist_cutoff=args.rna_contact_distance
        )

        rna_interactions = RNAInteractions(
            rna_contacts,
            minimum_strand_length=args.rna_minimum_strand_length,
        )

        writer = Writer(f"{base_path}/rna", args.model, args.rna_contact_distance)

        if args.soft_cutoff:
            graph_method = rna_interactions.soft_graph
        else:
            graph_method = rna_interactions.graph
        write_files(rna_model, graph_method, args.rna_dens_cutoff, writer)


def main():
    parser = argparse.ArgumentParser(description="RIBFIND")
    parser.add_argument("--model", help="A PDB file", required=True)
    parser.add_argument("--dssp", help="A DSSP file")
    parser.add_argument("--rnaml", help="An RNAML file")
    parser.add_argument(
        "--protein-cutoff-dist",
        help="A cutoff distance for side-chain interactions",
        dest="protein_contact_distance",
        default=6.5,
        type=float,
    )

    parser.add_argument(
        "--protein-helix-ratio",
        help="The length ratio above which, helices interact with one another",
        dest="protein_helix_ratio",
        default=0.4,
        type=float,
    )

    parser.add_argument(
        "--protein-dens-cutoff",
        help="The minimum number of SSEs for a cluster to be considered a rigid body.",
        dest="protein_dens_cutoff",
        default=3,
        type=int,
    )

    parser.add_argument(
        "--protein-minimum-strand-length",
        help="The minimum length of strands to be considered in interactions",
        dest="protein_minimum_strand_length",
        default=4,
        type=int,
    )

    parser.add_argument(
        "--rna-contact-dist",
        help="A cutoff distance for RNA interactions",
        dest="rna_contact_distance",
        default=7.5,
        type=float,
    )

    parser.add_argument(
        "--rna-minimum-strand-length",
        help="The minimum length of RNA strands to be considered in interactions",
        dest="rna_minimum_strand_length",
        default=4,
        type=int,
    )

    parser.add_argument(
        "--rna-dens-cutoff",
        help="The minimum number of SSEs for a cluster to be considered a rigid body.",
        dest="rna_dens_cutoff",
        default=3,
        type=int,
    )

    parser.add_argument(
        "--soft-cutoff",
        help="Use a soft cutoff between SSEs",
        dest="soft_cutoff",
        action="store_true",
    )
    parser.add_argument(
        "--output-dir",
        help="Optional directory to write output to",
        dest="output_dir",
        type=str,
        default=None,
    )

    parser.add_argument(
        "--version", action="version", version=f"RIBFIND v{ribfind.__version__}"
    )

    args = parser.parse_args()
    if args.dssp is None and args.rnaml is None:
        parser.error("Must provide an RNAML or DSSP file, or both")
    run(args)


if __name__ == "__main__":
    main()
