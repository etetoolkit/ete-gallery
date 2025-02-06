#!/usr/bin/env python3

"""
Example of SeqFace, sequence of amino acids.
First with default renderer, then with a random one for each sequence.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, SeqFace

from read_data import read_seqs


# Read an example tree.
t = Tree(open('../data/tree.nw'))


# Read related alignments and use them when drawing the nodes.
seqs = read_seqs('../data/tree.aln.faa')

# Show sequences with the default renderer (raster, which is faster).
def draw_node(node):
    if node.is_leaf:
        face = SeqFace(seqs[node.name], poswidth=10, draw_text=True, fs_max=15)
        yield Decoration(face, position='aligned')

layout = Layout(name='sequences (raster)',
                draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to show the same with a random renderer for each sequence.')
input()


# Show sequences with random renderer (svg or raster).
def draw_node_random_render(node):
    if node.is_leaf:
        face = SeqFace(seqs[node.name], poswidth=10, draw_text=True, fs_max=15,
                       render=random.choice(['svg', 'raster']))  # for fun :)
        yield Decoration(face, position='aligned')


layout_random_render = Layout(name='sequences (random)',
                              draw_node=draw_node_random_render)


t.explore(layouts=[BASIC_LAYOUT, layout_random_render])

print('Press enter to stop the server and finish.')
input()
