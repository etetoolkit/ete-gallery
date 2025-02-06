"""
Functions to read fasta files with sequences and pfam domains.
"""

def read_seqs(fastafile):
    """Read a fasta file and return a dict with seqs[id] = sequence.

    Example output: {'Phy003I7ZJ_CHICK': 'TMSQFNFSSAPAGGGFSFSTPKT...', ...}
    """
    seqs = {}
    for line in open(fastafile):
        if line.startswith('>'):
            sid = line.lstrip('>').rstrip()  # sequence id
            seqs[sid] = ''
        else:
            seqs[sid] += line.rstrip()

    return seqs


def read_pfams(fname):
    """Read pfam output file fname and return a dict from protein to domains.

    Example output: {leaf_name: [(domain1, start1, end1), ...], ...} like
        {'Phy003I7ZJ_CHICK': [('Nsp1_C', 7, 116)],
         'Phy0054BO3_MELGA': [('Nsp1_C', 3, 116)], ...}
    """
    pfams = {}  # dict that maps protein names to domains
    for line in open(fname):
        if line.startswith('#'):
            continue
        name, hit, _, _, _, start, end, _ = line.rstrip().split('\t', 7)
        pfams.setdefault(name, []).append( (hit, int(start), int(end)) )

    return pfams
