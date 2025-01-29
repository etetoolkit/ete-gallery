#!/usr/bin/env python3

"""
This is one of the simplest possible visualizations.
"""

from ete4 import Tree


t = Tree('(a:1,b:2);')

print('We have created a simple tree:')
print(t)

print('And we open it with the explorer using the default layout.')

t.explore()  # launches the backend server in another thread

print('Tree explorer is running. Press enter to stop the server and finish.')
input()  # after we press enter, the program finishes and the server closes
