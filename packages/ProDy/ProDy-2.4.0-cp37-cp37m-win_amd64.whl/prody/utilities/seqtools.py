"""This module defines functions and constants related to sequences."""

import re

__all__ = ['MATCH_SCORE', 'MISMATCH_SCORE', 'GAP_PENALTY',
           'GAP_EXT_PENALTY', 'ALIGNMENT_METHOD', 'splitSeqLabel',
           'alignBioPairwise']

MATCH_SCORE = 1.0
MISMATCH_SCORE = 0.0
GAP_PENALTY = -1.
GAP_EXT_PENALTY = -0.1
ALIGNMENT_METHOD = 'local'

SPLITLABEL = re.compile(r'[/-]+').split


def splitSeqLabel(label):
    """Returns label, starting residue number, and ending residue number parsed
    from sequence label."""

    try:
        if label.strip() == '':
            raise Exception
        idcode, start, end = SPLITLABEL(label)
    except Exception:
        return label, None, None
    else:
        try:
            return idcode, int(start), int(end)
        except Exception:
            return label, None, None


def alignBioPairwise(a_sequence, b_sequence,
                     ALIGNMENT_METHOD,
                     MATCH_SCORE, MISMATCH_SCORE,
                     GAP_PENALTY, GAP_EXT_PENALTY,
                     one_alignment_only=True):
    """
    Wrapper function to align two sequences using Biopython to support deprecation
    and associated warnings.

    It first attempts to use :mod:`Bio.Align.PairwiseAligner` and formats the output
    to match :mod:`Bio.pairwise2` methods and if it doesn't find it then it defaults
    back to :mod:`Bio.pairwise2` methods.

    :arg a_sequence: first sequence to align
    :type a_sequence: str

    :arg b_sequence: second sequence to align
    :type b_sequence: str

    :arg ALIGNMENT_METHOD: method for pairwise2 alignment
        Possible values are ``"local"`` and ``"global"``
    :type ALIGNMENT_METHOD: str

    :arg MATCH_SCORE: a positive integer, used to reward finding a match
    :type MATCH_SCORE: int

    :arg MISMATCH_SCORE: a negative integer, used to penalise finding a mismatch
    :type MISMATCH_SCORE: int

    :arg GAP_PENALTY: a negative integer, used to penalise opening a gap
    :type GAP_PENALTY: int

    :arg GAP_EXT_PENALTY: a negative integer, used to penalise extending a gap
    :type GAP_EXT_PENALTY: int

    :arg one_alignment_only: whether to return one alignment only or all generated
    :type one_alignment_only: bool
    """
    import numpy as np

    try:
        from Bio.Align import PairwiseAligner
        
        aligner = PairwiseAligner()
        aligner.mode = ALIGNMENT_METHOD
        aligner.match_score = MATCH_SCORE
        aligner.mismatch_score = MISMATCH_SCORE
        aligner.internal_open_gap_score = GAP_PENALTY
        aligner.internal_extend_gap_score = GAP_EXT_PENALTY
        alns = aligner.align(a_sequence, b_sequence)

        results = []
        for aln in alns:
            row_1 = aln.format().split("\n")[0].replace(" ", "-")
            row_2 = aln.format().split("\n")[2].replace(" ", "-")
            while len(row_1) < len(row_2):
                row_1 += "-"
            while len(row_2) < len(row_1):
                row_2 += "-"
            begin = max([np.where(np.array(list(row_1)) != "-")[0][0],
                         np.where(np.array(list(row_2)) != "-")[0][0]])
            end = (min([np.where(np.array(list(row_1)) != "-")[0][-1],
                        np.where(np.array(list(row_2)) != "-")[0][-1]]) - begin + 1)
            results.append((row_1, row_2, aln.score, begin, end))

        if one_alignment_only:
            return [results[0]]
        else:
            return results
        
    except (ImportError, AttributeError):
        from Bio import pairwise2

        if ALIGNMENT_METHOD == "local":
            return pairwise2.align.localms(a_sequence, b_sequence,
                                            MATCH_SCORE, MISMATCH_SCORE,
                                            GAP_PENALTY, GAP_EXT_PENALTY,
                                            one_alignment_only=1)
        elif ALIGNMENT_METHOD == "global":
            return pairwise2.align.globalms(a_sequence, b_sequence,
                                            MATCH_SCORE, MISMATCH_SCORE,
                                            GAP_PENALTY, GAP_EXT_PENALTY,
                                            one_alignment_only=1)
        else:
            raise ValueError("method should be local or global")
