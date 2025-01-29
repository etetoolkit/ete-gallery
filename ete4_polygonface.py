#!/usr/bin/env python3

from random import random, randint, choice

from ete4 import Tree
from ete4.smartview import (Layout, BASIC_LAYOUT, Decoration,
                            CircleFace, PolygonFace)

t = Tree()
t.populate(20, dist_fn=random, support_fn=random)

colors = ['red', 'blue', 'green']  # color to choose from

def draw_node(node):
    if node.is_leaf:
        face = PolygonFace(rmax=200, shape=choice([3,4,5,6,7,8]),
                           style={'fill': choice(colors)})
        yield Decoration(face, position='aligned')

        face2 = PolygonFace(rmax=200, shape=choice([3,4,5,6,7,8]),
                            style={'fill': choice(colors)})
        yield Decoration(face2, position='top', column=choice([0, 1]))

circles_layout = Layout(name='shapes', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, circles_layout])
input('Tree explorer running. Press enter to stop the server and finish.')
