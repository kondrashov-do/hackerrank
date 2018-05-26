#!/bin/python3

import math
import os
import random
import re
import sys

def ins_sort(arr):
    for i in range(1, len(arr)):
        j = i
        key = arr[j]
        while j > 0 and key < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr
# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()# = ins_sort(arr)
    #sorted(arr)
    #print(arr)
    if len(arr) < 2:
        return [0]
    min_distance = arr[1] - arr[0]
    result = []
    result.append(arr[1-0])
    result.append(arr[1])
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] < min_distance:
            #print(min_distance)
            #print(arr[i-1])
            #print(arr[i])
            min_distance = arr[i] - arr[i-1]
            result = []
            result.append(arr[i-1])
            result.append(arr[i])
        elif arr[i] - arr[i-1] == min_distance:
            result.append(arr[i-1])
            result.append(arr[i])
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
