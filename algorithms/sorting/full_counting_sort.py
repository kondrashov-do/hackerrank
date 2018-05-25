#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    result = [[] for i in range(100)]    
    for n_itr in range(n):
        xs = input().split()

        x = int(xs[0])

        s = xs[1]
        if n_itr < n / 2:
            result[x].append('-')
        else:
            result[x].append(s)
    for elem in result:
        if elem is not []:
            print(' '.join(elem), end=' ')
    
