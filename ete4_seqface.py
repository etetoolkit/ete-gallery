#!/usr/bin/env python3

"""
Exercising SeqFace.
"""

from ete4 import Tree
from ete4.smartview import BASIC_LAYOUT, Layout, Decoration, SeqFace

from read_data import read_seqs


# Read an example tree.
t = Tree(open('data/tree.nw'))


# Read related alignments and annotate the tree with them.
seqs = read_seqs('data/tree.aln.faa')

for node in t.leaves():
    node.props['seq'] = seqs[node.name]

def layout_seqface_draw_node(node):
    if node.is_leaf:
        face = SeqFace(
            node.props.get('seq'),
            poswidth=10,
            draw_text=True, fs_max=15)

        yield Decoration(face, position='aligned')


layout_seqface = Layout(name='seq',
                        draw_node=layout_seqface_draw_node) #, active=False)

t.explore(layouts=[BASIC_LAYOUT, layout_seqface])
input('Tree explorer running. Press enter to stop the server and finish.\n')


# TODO: Make a face to work for the code below.

def layout_alnface_gray(node):
    if node.is_leaf:
        face = AlignmentFace(
            node.props.get('seq'),
            seqtype='aa', gap_format='line', seq_format='[]',
            width=800, height=None,
            fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
            gap_linewidth=0.2,
            max_fsize=12, ftype='sans-serif',
            padding_x=0, padding_y=0)

        node.add_face(seq_face, position='aligned')

def layout_alnface_compact(node):
    if node.is_leaf:
        seq_face = AlignmentFace(
            node.props.get('seq'),
            seqtype='aa', gap_format='line', seq_format='compactseq',
            width=800, height=None,
            fgcolor='black', bgcolor='#bcc3d0', gapcolor='gray',
            gap_linewidth=0.2,
            max_fsize=12, ftype='sans-serif',
            padding_x=0, padding_y=0)

        node.add_face(seq_face, position='aligned')
