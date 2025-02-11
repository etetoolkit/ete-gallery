#!/usr/bin/env python3

"""
Tree style and node style with many options.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, BoxFace, PropFace, TextFace


# Let's create a tree with some extra properties.

random.seed(42)  # so we have the same trees in every run

t = Tree()
t.populate(50, dist_fn=random.random, support_fn=random.random)

for node in t.traverse():
    node.props['coolness'] = random.random()


# Custom layout, with draw_tree and draw_node.

def too_deep(node):
    return node.level > 5

tree_style = {
    'shape': 'circular',
    'radius': 2,
    'angle-start': -120,
    'angle-end': 120,
    'is-leaf-fn': too_deep,
    'show-popup-props': None,  # all available
    'hide-popup-props': ['dist'],
    'node-height-min': 15,
    'content-height-min': 10,
    'dot': {'shape': 'none'},
    'hz-line': 'wide-red',
    'vt-line': {'stroke': '#ffff00', 'stroke-width': 3},
    'box': {'fill': '#e0e0e0'},
    'aliases': {
        'support': {'fill': 'green'},  # used in default layout's support
        'myblue': {'fill': 'blue', 'font-weight': 'bold'},
        'wide-red': {'stroke': 'red', 'stroke-width': 5},
    }
}


def draw_node(node, collapsed):
    yield TextFace('visited node', position='bottom')

    yield PropFace('coolness', fmt='cool: %.2g', style='myblue',
                   position='bottom', column=1, anchor=(1, -1))

    if node.is_leaf:
        yield {'box': {'stroke-width': '4px',
                       'stroke': 'blue',
                       'fill': 'green'},
               'dot': {'fill': 'red',
                       'shape': 'hexagon',
                       'stroke': 'yellow',
                       'opacity': 1,
                       'radius': 20},
               'hz-line': {'stroke-width': 2}}
        yield BoxFace(wmax=80, hmax=70,
                      style={'fill': 'lightblue'},
                      text=f'node at depth {node.level}',
                      position='aligned')
    elif collapsed:
        yield BoxFace(wmax=80, hmax=70,
                      style={'fill': 'red'},
                      text='Collapsing nodes',
                      position='aligned')


layout = Layout(name='many',
                draw_tree=tree_style,
                draw_node=draw_node)


# Explore tree using basic layout and custom layout.

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
