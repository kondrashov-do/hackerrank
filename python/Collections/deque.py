from collections import deque
d = deque()
for _ in range(int(input())):
    in_string = input().split()
    #print('d.{0}({1})'.format(*in_string + ['x']))
    eval('d.{0}({1})'.format(*in_string + [' ']))
for elem in d:
    print(elem, end=" ")