#!/usr/bin/env python3

"""
Exercising SeqFace.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, SeqFace

from read_data import read_seqs


# Read an example tree.
t = Tree(open('data/tree.nw'))


# Read related alignments and annotate the tree with them.
seqs = read_seqs('data/tree.aln.faa')

for node in t.leaves():
    node.props['seq'] = seqs[node.name]

def layout_seqface_draw_node(node):
    if node.is_leaf:
        face = SeqFace(
            node.props.get('seq'),
            render=random.choice(['svg', 'raster']),  # for fun :)
            poswidth=10,
            draw_text=True, fs_max=15)

        yield Decoration(face, position='aligned')


layout_seqface = Layout(name='seq',
                        draw_node=layout_seqface_draw_node) #, active=False)

t.explore(layouts=[BASIC_LAYOUT, layout_seqface])
input('Tree explorer running. Press enter to stop the server and finish.\n')
