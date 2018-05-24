#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    swops = 0
    for i in range(1, len(arr)):
        j = i
        key = arr[j]
        while j > 0 and key < arr[j-1]:
            arr[j] = arr[j-1]
            swops += 1
            j -= 1
        arr[j] = key
    print(arr)
    return swops

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
