#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation1(n, queries):
    arr = [0 for i in range(n)]
    max_elem = arr[0]
    for query in queries:
        for i in range(query[0]-1, query[1]):
            arr[i] += query[2]
            max_elem = max(max_elem, arr[i])
    return max_elem

def arrayManipulation(n, queries):
    arr = [0 for i in range(n)]
    max_elem = 0
    elem_sum = 0
    for query in queries:
        arr[query[0]-1] += query[2]
        if (query[1] < len(arr)):
            arr[query[1]] -= query[2]
    for elem in arr:
        elem_sum += elem
        max_elem = max(max_elem, elem_sum)
    return max_elem

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
