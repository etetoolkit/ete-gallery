#!/usr/bin/env python3

"""
Example of SeqFace, sequence of amino acids.
"""

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, SeqFace

from read_data import read_seqs


# Read an example tree.
t = Tree(open('data/tree.nw'))


# Read related alignments and use them when drawing the nodes.
seqs = read_seqs('data/tree.aln.faa')

def draw_node(node):
    if node.is_leaf:
        face = SeqFace(seqs[node.name], poswidth=10, draw_text=True, fs_max=15)
        yield Decoration(face, position='aligned')

layout = Layout(name='seq', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
