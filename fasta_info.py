#!/usr/bin/env python3

"""
Give a summary of the contents of a fasta file.
"""

import sys
import os


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: %s <fasta_file>' % sys.argv[0])

    fname = sys.argv[1]

    seqs = read_fasta(fname)

    print('-', green('Fasta file:'), os.path.basename(fname))
    print('-', stats(seqs))
    print('-', green('Contents'), magenta('(number of omissions in parenthesis):'))
    print(summary_dict(seqs))



def summary_dict(d, max_lines=10, nhead=3, ntail=2):
    "Return a string summarizing the contents of a dict"
    # A dict with keys and values that are strings

    def to_lines(key_vals):
        return '\n'.join(cyan(summary_txt(key)) + f': {summary_txt(val)}'
                         for key, val in key_vals)

    key_vals = list(d.items())

    return (to_lines(key_vals) if len(d) < max_lines else
            (to_lines(key_vals[:nhead]) +
             magenta(f'\n[...({len(d) - nhead - ntail})]\n') +
             to_lines(key_vals[-ntail:])))


def summary_txt(txt, max_chars=25, nhead=10, ntail=5):
    "Return a shortened version of the given text"
    return (txt if len(txt) < max_chars else
            txt[:nhead] +
            magenta(f'[...({len(txt) - nhead - ntail})]') +
            txt[-ntail:])


def stats(d, max_chars=25):
    n = len(d)
    nkey_max = max(len(k) for k in d)
    nval_max = max(len(v) for v in d.values())
    return (green('Number of sequences: ') + str(n) + '    ' +
            green('Longest name: ') + f'{nkey_max} characters' + '    ' +
            green('Longest seq: ') + f'{nval_max} characters')


def read_fasta(fname):
    "Return a dict  d[name] = seq  with the contents of a fasta file"
    seqs = {}

    for line in open(fname):
        line = line.rstrip()  # remove trailing whitespace

        if not line or line.startswith(';'):
            pass
        elif line.startswith('>'):
            name = line[1:]
            seqs[name] = ''
        else:
            seqs[name] += line

    return seqs


def ansi(n):
    "Return function that escapes text with ANSI color n"
    return lambda txt: '\x1b[%dm%s\x1b[0m' % (n, txt)

black, red, green, yellow, blue, magenta, cyan, white = map(ansi, range(30, 38))



if __name__ == '__main__':
    main()
