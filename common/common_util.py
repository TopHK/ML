# -*-: encoding: utf-8 -*-
from collections import defaultdict
import operator


def get_count_of_list(sequence):
    """
    function: get count of each element in a list
    return value: dict
    """
    counts = defaultdict(int)
    for element in sequence:
        counts[element] += 1
    return counts


def top_count_of_list(sequence, num=0):
    """
    function: return top count of a list
    return value:
    """
    counts = get_count_of_list(sequence)
    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    if num == 0:
        return sorted_counts
    else:
        return sorted_counts[:num]

