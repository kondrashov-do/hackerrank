#!/bin/python3

import os
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    i = 0
    while i < n:
        print(a[(i + d)%n], end=" ")
        i += 1
