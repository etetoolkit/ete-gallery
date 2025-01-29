#!/usr/bin/env python3

"""
Use of draw_node(node, collapsed), and is_leaf_fn().
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, BoxFace, TextFace


t = Tree()
t.populate(30, dist_fn=random, support_fn=random)


# Add custom property.
for node in t.traverse():
    node.props['depth'] = node.level  # how deep we are in the tree


# Our example criteria to say when we consider a node a "leaf".
def too_deep(node):
    return node.level > 4


tree_style = {
    'show-popup-props': None,  # will show all properties in the nodes popup
    'hide-popup-props': ['dist'],  # except for 'dist'
    'is-leaf-fn': too_deep,
    'box': {'fill': 'blue', 'opacity': 0.1},
    'aliases': {
        'leaf': {'fill': 'green', 'stroke': 'green', 'opacity': 1},
    }
}


def draw_node(node, collapsed):
    if node.is_leaf:
        yield {'box': 'leaf',
               'dot': {'fill': 'red'}}  # set the node style

        yield TextFace('I am a leaf',  # add a face with its own style
                       style={'fill': 'white',
                              'stroke': 'black',
                              'stroke-width': 0.5})

    if collapsed:
        # Find the number of leaves in the collapsed nodes and show it.
        nleaves = sum(len(sibling) for sibling in collapsed)

        face = BoxFace(wmax=80, hmax=70,
                       style={'fill': 'red'},
                       text=f'I have {nleaves} leaves')

        yield Decoration(face, position='aligned')


rects_layout = Layout(name='rects',
                      draw_tree=tree_style,
                      draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, rects_layout])

print('Press enter to stop the server and finish.')
input()
