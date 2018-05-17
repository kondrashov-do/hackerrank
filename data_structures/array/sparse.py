#!/bin/python3

import os
import sys

#
# Complete the findSuffix function below.
#
def findSuffix(collections, queryString):
    result = 0
    for string in collections:
        if queryString == string:
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    q = int(input())

    for q_itr in range(q):
        queryString = input()

        res = findSuffix(strings, queryString)

        fptr.write(str(res) + '\n')

    fptr.close()
