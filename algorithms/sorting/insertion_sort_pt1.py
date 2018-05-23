#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    i = n-1
    value_to_sort = arr[i]
    while arr[i-1] > value_to_sort and i > 0:
        arr[i] = arr[i-1]
        print(' '.join([str(el) for el in arr]))
        i -= 1
        #print('i ', i)
    arr[i] = value_to_sort
    print(' '.join([str(el) for el in arr]))
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    insertionSort1(n, arr)
