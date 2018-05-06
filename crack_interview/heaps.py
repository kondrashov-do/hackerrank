#!/bin/python3

import sys
from heapq import heappush as push, heappushpop as pushpop

n = int(input().strip())
a = []
a_i = 0
min_heap = []
max_heap = []
lst_spliter = Spliter()
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    value = pushpop(min_heap, a_t)
    value = -pushpop(max_heap, -value)
    if len(min_heap) <= len(max_heap):
        push(min_heap, value)
    else:
        push(max_heap, -value)
    if len(min_heap) > len(max_heap):
        print(min_heap[0] / 1.)
    else:
        print((min_heap[0] - max_heap[0]) / 2.)
