#!/bin/python3

import sys

if __name__ == "__main__":
    s = input().strip()
    #print(s)
    alphabet_counter = []
    for i in range(ord('a'), ord('z')+1):
        alphabet_counter.append(0)
    for char in s:
        alphabet_counter[ord(char) - ord('a')] += 1
    for i in range(3):
        index = alphabet_counter.index(max(alphabet_counter))
        print(chr(index + 97), alphabet_counter[index])
        alphabet_counter[index] = 0