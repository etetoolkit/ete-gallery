#!/usr/bin/env python3

"""
Two columns in aligned panel.
"""

from random import random, choice

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, TextFace


t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


def draw_tree1(tree):
    yield Decoration(TextFace('holi del tree %d' % len(tree), rotation=-90),
                     position='header', column=1)

    yield Decoration(TextFace('despedidas', rotation=-45,
                              style={'fill': 'red'}),
                     position='header', column=2)


def draw_node1(node):
    if not node.is_leaf:
        return

    face = TextFace(choice(['hello', 'hi', 'hola', 'alo']))
    yield Decoration(face, position='aligned', column=1)

    face = TextFace(choice(['goodbye', 'bye', 'ciao', 'ta luego']))
    yield Decoration(face, position='aligned', column=2)

layout1 = Layout('1', draw_tree=draw_tree1, draw_node=draw_node1)



def draw_tree2(tree):
    yield Decoration(TextFace('see you 😊', rotation=-45,
                              style={'fill': 'green', 'stroke-width': 1}),
                     position='header', column=0)

def draw_node2(node):
    if not node.is_leaf:
        return

    face = TextFace(choice(['goodbye!', 'bye!', 'ciao!', 'ta luego!']))
    yield Decoration(face, position='aligned', column=0)

layout2 = Layout('2', draw_tree=draw_tree2, draw_node=draw_node2)


t.explore(layouts=[BASIC_LAYOUT, layout1, layout2])

print('Press enter to stop the server and finish.')
input()
