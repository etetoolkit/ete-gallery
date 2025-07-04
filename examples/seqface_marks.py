#!/usr/bin/env python3

"""
Example of SeqFace, sequence of amino acids, and some of them marked.
"""

import random

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, SeqFace

random.seed(42)


# Create a tree, add sequences (the property 'seq') and marks (the
# property 'marks') to its leaves.

t = Tree()
t.populate(20, dist_fn=random.random, support_fn=random.random)

def create_random_seq(n):
    return [random.choice('-ACDEFGHIKLMNPQRSTVWXY') for _ in range(n)]

for node in t.leaves():
    node.props['seq'] = create_random_seq(100)  # 100 amino acids
    node.props['marks'] = [random.randint(2, 6),
                           random.randint(11, 19)]  # 2 marks

# Draw sequences and the marked positions.
def draw_node(node):
    if node.is_leaf:
        yield SeqFace(node.props['seq'],
                      marks=node.props['marks'],
                      position='aligned')


layout = Layout(name='sequences and marks', draw_node=draw_node)

t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
