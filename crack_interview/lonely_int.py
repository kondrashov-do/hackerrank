#!/bin/python3

import sys

def lonely_integer(a):
    '''bin_arr = [False] * 100
    for number in a:
        bin_arr[number] = bin_arr[number] ^ True
    for i in range(100):
        if bin_arr[i]:
            return i'''
    value = 0
    for number in a:
        value ^= number
    return value
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))