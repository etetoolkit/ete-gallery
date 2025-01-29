#!/usr/bin/env python3

from random import random, choice

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, RectFace

t = Tree()
t.populate(20, dist_fn=random, support_fn=random)

def draw_node(node):
    if node.is_leaf:
        face = RectFace(wmax=80, hmax=70,
                        style={'fill': 'blue'})
        yield Decoration(face, position='top', column=choice([0,1]))

rects_layout = Layout(name='rects', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, rects_layout])
input('Tree explorer running. Press enter to stop the server and finish.\n')
