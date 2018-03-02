from itertools import combinations
l= list(input().split())
input_string = sorted(l[0])
for k in range(1, int(l[1])+1):
    for item in combinations(input_string, k):
        print(''.join(item))