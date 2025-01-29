#!/usr/bin/env python3

"""
This is one of the simplest possible visualizations.
"""

from ete4 import Tree

# First some explanation.

print('This is a tutorial to show ete\'s graphical capabilities.\n'
      'Some steps are commented in messages like this.\n'
      'The idea is not to just run the files, but to look at their source too.')
print('Press enter to continue.')
input()


# Then we create a simple tree and show it on the screen.
t = Tree('(a:1,b:2);')

print('We have created a simple tree:')
print(t)

# Finally, we explore it.
print('And we open it with the explorer using the default layout.')

t.explore()  # launches the backend server in another thread

print('Tree explorer is running. Press enter to stop the server and finish.')
input()  # after we press enter, the program finishes and the server closes
