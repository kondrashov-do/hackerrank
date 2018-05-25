#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count_arr = [0  for i in range(100)]
    for elem in arr:
        count_arr[elem] += 1
    arr = []
    for indx, elem in enumerate(count_arr):
        while elem > 0:
            arr.append(indx)
            elem -= 1
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
