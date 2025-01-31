#!/usr/bin/env python3

"""
Example of use of CircleFace.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, CircleFace

random.seed(42)  # so we have the same trees in every run


# Tree randomly populated.

t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)


# Layout with draw_node() that draws aligned circles on leaves.

colors = ['red', 'blue', 'green']  # color to choose from

def draw_node(node):
    if node.is_leaf:
        face = CircleFace(rmax=random.randint(2, 20),
                          style={'fill': random.choice(colors)})
        yield Decoration(face, position='aligned')


circles_layout = Layout(name='circles', draw_node=draw_node)


# Launch the explorer.

t.explore(layouts=[BASIC_LAYOUT, circles_layout])

print('Press enter to stop the server and finish.')
input()
