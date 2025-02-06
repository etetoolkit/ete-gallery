#!/usr/bin/env python3

from ete4 import Tree
from ete4.smartview import Layout, BASIC_LAYOUT, TextFace, Decoration


nw = '((A:1,B:1)internal_nodeF:1,(C:1,(D:1,E:1)internal_nodeG:1)internal_nodeH:1)root:1;'

t = Tree(nw, parser=1)


def draw_node(node, collapsed):
    name = node.props.get('name')

    if not name:
        return

    if collapsed:
        text_face = TextFace(name + '_aligned_column1_collapsed-only',
                             style={'fill': 'green'},
                             fs_min=6, fs_max=25)
        yield Decoration(text_face, position='aligned', column=1)
        return

    if node.is_leaf:
        text_face = TextFace(name + '_aligned_column0',
                             style={'fill': 'green'},
                             fs_min=6, fs_max=25)
        yield Decoration(text_face, position='aligned', column=0)
    else: # internal node or root
        text_face = TextFace(name + '_aligned_column1',
                             style={'fill': 'green'},
                             fs_min=6, fs_max=25)
        yield Decoration(text_face, position='aligned', column=1)

    text_face = TextFace(name + '_branch-right',
                         style={'fill': 'red'},
                         fs_min=6, fs_max=25)
    yield Decoration(text_face, position='right')

    text_face = TextFace(name + '_branch-top',
                         style={'fill': 'blue'},
                         fs_min=6, fs_max=25)
    yield Decoration(text_face, position='top')

    text_face = TextFace(name + '_branch-bottom',
                         style={'fill': 'brown'},
                         fs_min=6, fs_max=25)
    yield Decoration(text_face, position='bottom')


layout = Layout(name='text face with nodename', draw_node=draw_node)


t.explore(layouts=[BASIC_LAYOUT, layout])
input('Tree explorer running. Press enter to stop the server and finish.\n')
