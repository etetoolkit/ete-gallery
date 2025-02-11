#!/usr/bin/env python3

"""
Example of a big tree with long sequences.
Tree with 50k leaves, each node with sequences of 1.5k positions.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, SeqFace

random.seed(42)  # so we have the same trees in every run


print('Creating random tree with 10k leaves...')

t = Tree()
t.populate(10_000, dist_fn=random.random, support_fn=random.random)


print('Annotating every node with a random sequence of 1500 aas...')

def create_random_seq(n):
    return ''.join(random.choice('-ACDEFGHIKLMNPQRSTVWXY') for _ in range(n))

for node in t.traverse():
    node.props['seq'] = create_random_seq(1500)


print('Drawing...')

def draw_node(node):
    if node.is_leaf:
        yield SeqFace(node.props.get('seq'),
                      poswidth=10, draw_text=True, fs_max=15,
                      position='aligned')

layout = Layout(name='seq', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
