#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    seq_list = []
    result = []
    for i in range(n):
        seq_list.append([])
    print(seq_list)
    last_answer = 0
    for query in queries:
        x = query[1]
        y = query[2]
        if query[0] == 1:
            seq_list[(x^last_answer) % n].append(y)
        if query[0] == 2:
            last_answer = seq_list[(x^last_answer) % n][y % len(seq_list[(x^last_answer) % n])]
            result.append(last_answer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
