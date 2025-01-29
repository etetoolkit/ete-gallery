#!/usr/bin/env python3

"""
Collapsed nodes as outline.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, TextFace

random.seed(42)  # so we have the same trees in every run

t = Tree()
t.populate(50, dist_fn=random.random, support_fn=random.random)


tree_style = {
    'collapsed': {
        'shape': 'outline',
        'stroke': '#0000FF',
        'stroke-width': 3,
        'fill': '#303030',
        'opacity': 0.5,
    },
}

def draw_node(node, collapsed):
    if not collapsed:
        yield Decoration(TextFace('Not collapsed'),
                         position='bottom', column=1, anchor=(1, -1))

layout = Layout(name='outline tricks',
                draw_tree=tree_style,
                draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
