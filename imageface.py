#!/usr/bin/env python3

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, ImageFace

t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)


images = ['data/'+x for x in ['python.jpg', 'ete.png', 'frog.jpeg']]

def draw_node(node):
    if node.is_leaf:
        face = ImageFace(path=random.choice(images), wmax=100)

        yield Decoration(face, position='aligned')

        yield Decoration(face, position='top')


layout = Layout(name='sample1', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])
input('Tree explorer running. Press enter to stop the server and finish.\n')
