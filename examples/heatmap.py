#!/usr/bin/env python3

"""
Example of HeatmapFace.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, HeatmapFace

random.seed(42)  # so we have the same trees in every run


# Tree randomly populated.

t = Tree()
t.populate(50, dist_fn=random.random, support_fn=random.random)


def draw_node(node):
    if node.is_leaf:
        values = [random.randint(-100, 100) for _ in range(80)]
        yield HeatmapFace(values,
                          value_range=(0, 100),
                          color_range=('#f00', '#0f0'),
                          position='aligned')

layout = Layout(name='heatmap', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
