#!/usr/bin/env python3

"""
Nucleotides.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, SeqFace

from read_data import read_seqs


t = Tree()
t.populate(5_000, dist_fn=random.random, support_fn=random.random)


def create_random_seq(n):
    return ''.join(random.choice('-ACGTU') for _ in range(n))

for node in t.traverse():
    node.props['seq'] = create_random_seq(150)


def layout_seqface_draw_node(node):
    if node.is_leaf:
        face = SeqFace(
            node.props.get('seq'),
            seqtype='nt',
            poswidth=10,
            draw_text=True,
            fs_max=15)

        yield Decoration(face, position='aligned')

layout_seqface = Layout(name='seq', draw_node=layout_seqface_draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout_seqface])
input('Tree explorer running. Press enter to stop the server and finish.\n')
