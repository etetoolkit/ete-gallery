#!/usr/bin/env python3

"""
Example of SeqFace, sequence of nucleotides.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, SeqFace

from read_data import read_seqs

random.seed(42)  # so we have the same trees in every run


# Create a tree and add the 'seq' property to its nodes.
t = Tree()
t.populate(5_000, dist_fn=random.random, support_fn=random.random)


def create_random_seq(n):
    return ''.join(random.choice('-ACGTU') for _ in range(n))

for node in t.traverse():
    node.props['seq'] = create_random_seq(150)


# Create a layout that draws sequences aligned with the leaves.
def draw_node(node):
    if node.is_leaf:
        face = SeqFace(
            node.props.get('seq'),
            seqtype='nt',  # nucleotides (the other option being 'aa')
            poswidth=10,
            draw_text=True,
            fs_max=15)

        yield Decoration(face, position='aligned')

layout = Layout(name='seq', draw_node=draw_node)


# Launch the explorer.
t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
