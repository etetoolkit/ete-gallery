#!/usr/bin/env python3

"""
Layout with draw_node() that generates styles (dicts) and faces.
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, TextFace


t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


def draw_node(node):
    if node.is_leaf:
        yield {'box': {'fill': 'lightblue'}}  # set style of the node box
    else:
        yield TextFace('I am an inner node', column=2)  # add face


layout = Layout(name='blue leaves', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
