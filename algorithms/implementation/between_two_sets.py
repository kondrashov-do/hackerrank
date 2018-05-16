#!/bin/python3

import os
import sys

# define gcd function
def gcd(x, y):
    """This function implements the Euclidian algorithm
    to find G.C.D. of two numbers"""

    while(y):
        x, y = y, x % y
    return x

# define lcm function
def lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""
    lcm = (x*y)//gcd(x,y)
    return lcm
    
#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    lcm_a = a[0]
    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])
    print('lcm_a', lcm_a)    
    gcd_b = b[0]
    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])
    print('gcd_b', gcd_b)
    result = 0
    for i in range(lcm_a, gcd_b+1, lcm_a):
        if gcd_b % i == 0:
            result += 1
    return result
    

    
            
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
