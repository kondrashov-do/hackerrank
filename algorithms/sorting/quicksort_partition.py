#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    pivot = arr[0]
    equal = []
    
    left = []
    right = []
    for elem in arr:
        if elem == pivot:
            equal.append(elem)
        elif elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
    result = []
    result.extend(left)
    result.extend(equal)
    result.extend(right)
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
