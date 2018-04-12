#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    index_min = 0
    index_max = 0
    min = arr[0]
    max = arr[0]
    min_sum = 0
    max_sum = 0
    for i, num in enumerate(arr):
        if arr[i] > max:
            max = arr[i]
            index_max = i
        if arr[i] < min:
            min = arr[i]
            index_min = i
    for i,num in enumerate(arr):
        if i != index_min:
            max_sum +=arr[i]
        if i != index_max:
            min_sum +=arr[i]
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)