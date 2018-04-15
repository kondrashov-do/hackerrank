#!/bin/python3

import sys

def super_reduced_string(s):
    i = 1
    while i < len(s):
        if s[i] == s[i-1]:
            s = s[0:i-1] + s[i+1:]
            i = 0
        i += 1
    if len(s) == 0:
        return 'Empty String'
    else:
        return s
            
            

s = input().strip()
result = super_reduced_string(s)
print(result)
