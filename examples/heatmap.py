#!/usr/bin/env python3

"""
Example of HeatmapFace.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, HeatmapFace

# Read an example tree.
t = Tree(open('../data/tree.nw'))


def draw_node(node):
    if node.is_leaf:
        face = HeatmapFace([random.randint(0, 10) for _ in range(20)],
                           (0, 10), ('000000', 'ffffff'))
        yield Decoration(face, position='aligned')

layout = Layout(name='heatmap', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
