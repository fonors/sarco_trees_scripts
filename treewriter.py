#!/usr/bin/env python3
'''
    Tree Writer - Write phylogenetic trees as an SVG file
    Copyright (C) 2024  fonors, goncalof21, MadalenaFranco2 & scmdcunha

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import argparse
import toytree, toyplot.svg
import numpy as np

parser = argparse.ArgumentParser(
                    prog = 'Tree Writer',
                    description = 'Write phylogenetic trees as an SVG file.')

def tree_args(argparser):
    """
    Gets the arguments the user defined when running the script and returns them.
    """
    argparser.add_argument("-i", "--input", help="Input tree file.")
    argparser.add_argument("-o", "--output", help="Output SVG file.")
    argparser.add_argument("-r", "--root", help="Tree's root branch/outgroup.")

    tree_args = argparse.parse_args()
    return tree_args

def tree_render(args):
    """
    Takes the input, output and root arguments and draws the tree into an SVG file.
    """
    tree = toytree.tree(args.input)
    rtree = tree.root(args.root)

    canvas, axes, mark = rtree.draw(node_hover=True, node_sizes=16, tip_labels_align=True, node_labels='support', use_edge_lengths=False)

    toyplot.svg.render(canvas, args.output)

if __name__ == "__main__":
    user_args = tree_args(parser)
    tree_render(user_args)
