#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    #print(arr)
    for indx in range(1, n):
        i = indx
        value_to_sort = arr[i]
        while value_to_sort < arr[i-1] and i > 0:
            arr[i] = arr[i-1]  
            i -= 1
        arr[i] = value_to_sort
        print(' '.join([str(el) for el in arr]))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
