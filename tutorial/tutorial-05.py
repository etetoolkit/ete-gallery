#!/usr/bin/env python3

"""
Layout with draw_node() that generates faces.
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, TextFace


t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


def draw_node(node):
    if not node.is_leaf:
        # We can yield elements, or return a list with all at the end.
        yield TextFace('I am an inner node!')  # a "face" with default position
    else:
        yield TextFace('I am a leaf!', position='right')

    if node.is_root:
        yield TextFace('it all starts here',
                       style={'fill': 'blue'},  # faces can have styles
                       position='left')


layout = Layout(name='texts on different positions', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
