#!/bin/python3

import os
import sys

def fruit_count(s, t, tree_postion, fruits):
    fruit_count = 0
    for fruit in fruits:
        fruit_position = tree_postion + fruit
        if fruit_position >= s and fruit_position <= t:
            fruit_count += 1
    return fruit_count

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count  = fruit_count(s,t,a,apples)
    orange_count = fruit_count(s,t,b,oranges)
    print(apple_count)
    print(orange_count)
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
