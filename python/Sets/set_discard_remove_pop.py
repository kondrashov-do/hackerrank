n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    in_string = input().split()
    #print(in_string)
    eval('s.{0}({1})'.format(*in_string + ['']))
print(sum(s))