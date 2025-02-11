#!/usr/bin/env python3

"""
Tree style and node style with many options passed as arguments to explore().
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


# Custom layout
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


layout = Layout(name='many', draw_node=draw_node)


# Explore tree using basic layout and custom layout, and extra arguments.

t.explore(layouts=[BASIC_LAYOUT, layout],
          shape='circular',
          radius=2,
          angle_start=-120,
          angle_end=120,
          is_leaf_fn=lambda node: node.level > 5,
          show_popup_props=None,  # all available
          hide_popup_props=['dist'],
          node_height_min=15,
          content_height_min=10,
          dot={'shape': 'none'},
          hz_line='wide-red',
          vt_line={'stroke': '#ffff00', 'stroke-width': 3},
          box={'fill': '#e0e0e0'},
          aliases={
              'support': {'fill': 'green'},  # used in default layout's support
              'myblue': {'fill': 'blue', 'font-weight': 'bold'},
              'wide-red': {'stroke': 'red', 'stroke-width': 5},
          })

print('Press enter to stop the server and finish.')
input()
