#!/bin/python3

import sys

def solve(arr, money):
    ice_cream_map = {}
    for i in range(len(arr)):
        if arr[i] < money:
            first_flavor = arr[i]
            second_flavor = money - arr[i]
            if second_flavor in ice_cream_map:
                 print(ice_cream_map[second_flavor]+1, i+1)
            else:
                ice_cream_map[first_flavor] = i
            

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)