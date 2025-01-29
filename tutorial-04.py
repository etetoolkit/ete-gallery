#!/usr/bin/env python3

"""
Layout using the draw_node() function.
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, TextFace


t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


def draw_node(node):
    if node.is_leaf:
        return TextFace('I am a leaf!')  # a single return is fine


layout = Layout(name='simple text on leaves', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
