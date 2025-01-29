#!/usr/bin/env python3

"""
Two columns in aligned panel.
"""

from random import random, choice

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, TextFace


t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


def draw_node1(node):
    if not node.is_leaf:
        return

    face = TextFace(choice(['hello', 'hi', 'hola', 'alo']))
    yield Decoration(face, position='aligned', column=1)

    face = TextFace(choice(['goodbye', 'bye', 'ciao', 'ta luego']))
    yield Decoration(face, position='aligned', column=2)

layout1 = Layout('1', draw_node=draw_node1)


def draw_node2(node):
    if not node.is_leaf:
        return

    face = TextFace(choice(['xhello', 'xhi', 'xhola', 'xalo']))
    yield Decoration(face, position='aligned', column=1)

    face = TextFace(choice(['xgoodbye', 'xbye', 'xciao', 'xta luego']))
    yield Decoration(face, position='aligned', column=0)

layout2 = Layout('2', draw_node=draw_node2)


t.explore(layouts=[layout1, layout2])

print('Press enter to stop the server and finish.')
input()
