#!/usr/bin/env python3

"""
Layout with a tree style.

See possible attributes for style in:
https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute
"""

from random import random

from ete4 import Tree
from ete4.smartview import Layout


# Simple layout.

t = Tree()
t.populate(10, dist_fn=random, support_fn=random)


print('We will add a simple layout, with only a tree style.')

tree_style = {
    'hz-line': {  # style of node horizontal lines (length lines)
        'stroke': 'red',  # we can name colors by their common name
    },
    'vt-line': {  # style of node vertical lines (lines towards children)
        'stroke': '#0000ff',  # we can name colors by their html code
        'stroke-width': 1.5,  # and we can change the width
    },
    'box': {  # style of the boxes surrounding nodes
        'fill': '#dddddd',  # changes the interior color
        'opacity': 0.4,  # we can control its opacity too
    },
}


layout = Layout('example_tree_style', draw_tree=tree_style)

t.explore('only our layout', layouts=[layout])

print('Since we give layouts explicitely, it will not use the default layout.')

print('Press enter to add the default layout.')
input()


# Adding the default layout.

print('To use the default layout too (with leaf names, branch distance and '
      'support), we can add it explicitely when exploring the tree.')

from ete4.smartview import BASIC_LAYOUT

t.explore('default layout and our layout', layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
