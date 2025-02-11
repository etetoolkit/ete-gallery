#!/usr/bin/env python3

"""
Example of representing collapsed nodes.

They will be outlined (instead of with a skeleton), and different
faces will be used for collapsed/uncollapsed nodes.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, TextFace

random.seed(42)  # so we have the same trees in every run


t = Tree()
t.populate(50, dist_fn=random.random, support_fn=random.random)


# This tree style will specify how to show collapsed nodes.
tree_style = {
    'collapsed': {  # we set the style of collapsed nodes
        'shape': 'outline',  # use a triangle outlining the nodes
        'stroke': '#0000FF',  # with blue surroundings
        'stroke-width': 3,  # and kind of thick
        'fill': '#303030',  # all filled with gray
        'opacity': 0.5,  # and a bit transparent
    },
}

# This draw_node function specifies what to do with collapsed nodes
# when drawing them. Note that it is draw_node(node, collapsed) and
# not just draw_node(node). When we receive the second argument, it is
# a list of the collapsed (sibling) nodes, if any.
def draw_node(node, collapsed):
    if not collapsed:  # add a little text to the bottom-right
        yield TextFace('Not collapsed',
                       position='bottom', column=1, anchor=(1, -1))

layout = Layout(name='collapsed tricks',
                draw_tree=tree_style,
                draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
