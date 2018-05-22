#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting1(unsorted):
    for i in range(len(unsorted) - 1):
        min_el_int = int(unsorted[i])
        min_el = unsorted[i]
        min_in = i
        for j in range(i+1, len(unsorted)):
            if int(unsorted[j]) < min_el_int:
                min_el_int = int(unsorted[j])
                min_el = unsorted[j]
                min_in = j
        temp = unsorted[i]
        unsorted[i] = min_el
        unsorted[min_in] = temp
    return unsorted

def partition(array, lo, hi):
    pivot = lo
    for i in range(lo+1, hi+1):
        if array[i] <= array[lo]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[lo] = array[lo], array[pivot]
    return pivot

def quicksort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quicksort(array, lo, p-1)
        quicksort(array, p+1, hi)

def bigSorting2(unsorted):
    unsorted = [int(el) for el in unsorted]
    quicksort(unsorted, 0, len(unsorted)-1)
    print('OUTPUT: ', unsorted)
    unsorted = [str(el) for el in unsorted]
    return unsorted

def bigSorting(unsorted):
    return sorted(unsorted, key=int)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
