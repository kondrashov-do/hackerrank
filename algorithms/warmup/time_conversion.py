#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hh = s[:2]
    mm = s[3:5]
    ss = s[6:8]
    indicator = s[8]
    if indicator == 'A':
        if hh != '12':
            return(hh+':'+mm+':'+ss)
        else:
            return('00:'+mm+':'+ss)
    else:
        if hh != '12':
            hh = int(hh) + 12
            return(str(hh)+':'+mm+':'+ss)
        else:
            return('12:'+mm+':'+ss)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()