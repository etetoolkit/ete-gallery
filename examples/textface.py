#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, TextFace


nw = '((A:1,B:1)internal_F:1,(C:1,(D:1,E:1)internal_G:1)internal_H:1)root:1;'

t = Tree(nw, parser=1)


def draw_node(node, collapsed):
    name = node.props.get('name')

    if not name:
        return

    if collapsed:
        yield TextFace(name + '_aligned_column1_collapsed-only',
                       style={'fill': 'green'},
                       fs_min=6, fs_max=25,
                       position='aligned', column=1)
        return

    if node.is_leaf:
        yield TextFace(name + '_aligned_column0',
                       style={'fill': 'green'},
                       fs_min=6, fs_max=25,
                       position='aligned', column=0)
    else: # internal node or root
        yield TextFace(name + '_aligned_column1',
                       style={'fill': 'green'},
                       fs_min=6, fs_max=25,
                       position='aligned', column=1)

    yield TextFace(name + '_branch-right',
                   style={'fill': 'red'},
                   fs_min=6, fs_max=25,
                   position='right')

    yield TextFace(name + '_branch-top',
                   style={'fill': 'blue'},
                   fs_min=6, fs_max=25,
                   position='top')

    yield TextFace(name + '_branch-bottom',
                   style={'fill': 'brown'},
                   fs_min=6, fs_max=25,
                   position='bottom')

layout = Layout(name='text face with nodename', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])

print('Press enter to stop the server and finish.')
input()
