#!/usr/bin/env python3

"""
SeqFace example.
"""

import random

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, Decoration, SeqFace

random.seed(42)  # so we have the same trees in every run

t = Tree()
t.populate(50, dist_fn=random.random, support_fn=random.random)

aminoacids = 'GAVLITSMCPFYWHKRDENQ'
# See https://www.ebi.ac.uk/pdbe/docs/roadshow_tutorial/msdtarget/AAcodes.html

def draw_node(node, collapsed):
    if node.is_leaf:
        seq = [random.choice(aminoacids) for _ in range(20)]
        yield Decoration(SeqFace(seq, hmax=20), position='aligned')

layout = Layout(name='seqface example',
                draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
