#!/bin/python3

import math
import os
import random
import re
import sys

def calculate_sum(arr, r, c):
    result = 0
    for i in range(3):
        result += arr[r][c+i]
        result += arr[r+2][c+i]
    result += arr[r+1][c+1]
    return result

# Complete the array2D function below.
def array2D(arr):
    length = 6
    max_sum = calculate_sum(arr, 0, 0)
    for i in range(length - 2):
        for j in range(length - 2):
            max_sum = max(max_sum, calculate_sum(arr, i, j))
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
