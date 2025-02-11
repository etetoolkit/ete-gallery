#!/usr/bin/env python3

"""
Example of headers in the aligned panel (and values in their
corresponding columns).

Also, combining two layouts that both have aligned headers and values.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, TextFace

random.seed(42)  # so we have the same trees in every run


t = Tree()
t.populate(10, dist_fn=random.random, support_fn=random.random)


# We will use 2 layouts, each one with:
#   - draw_tree putting headers (TextFaces in position 'header', different columns)
#   - draw_node putting values in several columns

# Layout 1. It writes serious information in aligned columns 1 and 2.

def draw_tree1(tree):
    yield TextFace('seq type', rotation=-90,
                   position='header', column=1)

    yield TextFace('matches', rotation=-45,
                   style={'fill': 'red'},
                   position='header', column=2)

def draw_node1(node):
    if not node.is_leaf:
        return

    yield TextFace(random.choice(['dna', 'amino acids', 'tokens']),
                   position='aligned', column=1)

    yield TextFace(str(random.randint(0, 200)),
                   position='aligned', column=2)

layout1 = Layout('1', draw_tree=draw_tree1, draw_node=draw_node1)


# Layout 2. It writes silly information in aligned column 0.

def draw_tree2(tree):
    yield TextFace('greeting 😊', rotation=-45,
                   style={'fill': 'green', 'stroke-width': 1},
                   position='header', column=0)

def draw_node2(node):
    if not node.is_leaf:
        return

    yield TextFace(random.choice(['hi!', 'hey you!', 'welcome!', 'do join!']),
                   position='aligned', column=0)

layout2 = Layout('2', draw_tree=draw_tree2, draw_node=draw_node2)


# Explore tree combining both layouts.

t.explore(layouts=[BASIC_LAYOUT, layout1, layout2])

print('Press enter to stop the server and finish.')
input()
