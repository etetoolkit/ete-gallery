#!/usr/bin/env python3

from random import random, randint, choice

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, CircleFace

t = Tree()
t.populate(20, dist_fn=random, support_fn=random)

colors = ['red', 'blue', 'green']  # color to choose from

def draw_node(node):
    if node.is_leaf:
        face = CircleFace(rmax=randint(2, 20),
                          style={'fill': choice(colors)})
        yield Decoration(face, position='aligned')

circles_layout = Layout(name='circles', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, circles_layout])
input('Tree explorer running. Press enter to stop the server and finish.')
