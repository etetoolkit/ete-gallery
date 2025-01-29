#!/usr/bin/env python3

"""
Two trees.
"""

from random import random

from ete4 import Tree


# First tree.

print('Creating and exploring the first tree.')

t = Tree('(a:1,b:2);')

t.explore()  # we don't give it a name (it will get one automatically)

print('Press enter to add the next tree.')
input()


# Second tree.

print('Creating and exploring a second tree.')

t2 = Tree()
t2.populate(10, dist_fn=random, support_fn=random)

t2.explore('I am the new tree - click me!')  # we give it a name

print('Press enter to stop the server and finish.')
input()
