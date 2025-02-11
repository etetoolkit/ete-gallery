#!/usr/bin/env python3

"""
Example of use of RectFace.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, RectFace

random.seed(42)  # so we have the same trees in every run


t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)

def draw_node(node):
    if node.is_leaf:
        yield RectFace(wmax=80, hmax=70,
                       style={'fill': 'blue', 'opacity': 0.7},
                       position='top',
                       column=random.choice([0, 1]))  # some will superimpose

layout = Layout(name='rects', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
