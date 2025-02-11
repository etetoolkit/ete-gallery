#!/usr/bin/env python3

"""
Example of use of ImageFace.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, ImageFace

random.seed(42)  # so we have the same trees in every run


t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)


images = ['../data/'+x for x in ['python.jpg', 'ete.png', 'frog.jpeg']]

def draw_node(node):
    if node.is_leaf:
        yield ImageFace(path=random.choice(images), wmax=100,
                        position='aligned')  # put the image aligned

        yield ImageFace(path=random.choice(images), wmax=100,
                        position='top')  # and also on top of the branch

layout = Layout(name='sample1', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
