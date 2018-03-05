from collections import defaultdict
d = defaultdict(list)
l = list()
n, m = map(int, input().split())
for i in range(1, n+1):
    d[input()].append(str(i))
    for i in range(1, m+1):
            element = input()
            if element in d:
                print(' '.join(d[element]))
            else:
                print(-1)
