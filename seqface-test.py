#!/usr/bin/env python3

"""
50k nodes
Each node with sequences associated of 1.5k positions
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, SeqFace


print('Creating random tree with 50k nodes...')

t = Tree()
t.populate(50_000, dist_fn=random.random, support_fn=random.random)


print('Annotating every node with a random sequence of 1500 aas...')

def create_random_seq(n):
    return ''.join(random.choice('-ACDEFGHIKLMNPQRSTVWXY') for _ in range(n))

for node in t.traverse():
    node.props['seq'] = create_random_seq(1500)


print('Drawing...')

def layout_seqface_draw_node(node):
    if node.is_leaf:
        face = SeqFace(
            node.props.get('seq'),
            poswidth=10,
            draw_text=True, fs_max=15)

        yield Decoration(face, position='aligned')

layout_seqface = Layout(name='seq', draw_node=layout_seqface_draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout_seqface])
input('Tree explorer running. Press enter to stop the server and finish.\n')
