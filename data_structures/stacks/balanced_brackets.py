#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    result = 'NO'
    stack = []
    for symbol in s:
        if len(stack) > 0:
            if symbol == '}' and stack[-1] == '{':
                stack.pop()
            elif symbol == ']' and stack[-1] == '[':
                stack.pop()
            elif symbol == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(symbol)
        else:
            stack.append(symbol)
    if len(stack) == 0:
        result = 'YES'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()