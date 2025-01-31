#!/usr/bin/env python3

"""
Example of use of PolygonFace.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, PolygonFace

random.seed(42)  # so we have the same trees in every run


t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)


colors = ['red', 'blue', 'green']  # color to choose from

def draw_node(node):
    if node.is_leaf:
        face = PolygonFace(rmax=200, shape=random.choice([3, 4, 5, 6, 7, 8]),
                           style={'fill': random.choice(colors)})
        yield Decoration(face, position='aligned')

        face2 = PolygonFace(rmax=200, shape=random.choice([3, 4, 5, 6, 7, 8]),
                            style={'fill': random.choice(colors)})
        yield Decoration(face2, position='top',
                         column=random.choice([0, 1]))  # for variety

layout = Layout(name='shapes', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
