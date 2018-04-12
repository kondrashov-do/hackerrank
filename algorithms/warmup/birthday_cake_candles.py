#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    max_height = ar[0]
    count_max_height = 0
    for candle in ar:
        if candle > max_height:
            max_height = candle
            count_max_height = 0
        if candle == max_height:
            count_max_height += 1
    return count_max_height 	

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()
