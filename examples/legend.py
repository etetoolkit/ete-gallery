#!/usr/bin/env python3

"""
Example of using legends.
"""

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, LegendFace


t = Tree('((a,b),c);')

def draw_tree(tree):
    yield LegendFace(title='random type',
                     variable='discrete',
                     colormap={'a': 'red', 'b': 'blue', 'c': 'green'})

    yield LegendFace(title='sample1',
                     variable='continuous',
                     value_range=(0, 100),
                     color_range=('#0000ff', '#ffffff', '#ff0000'))

    yield LegendFace(title='yet another legend',
                     variable='discrete',
                     colormap={'one': '#129933', '2': 'blue', 'three': 'cyan'})

layout = Layout('Layout with legend', draw_tree=draw_tree)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
