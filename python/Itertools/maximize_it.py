from itertools import product
K, M = map(int, input().split())
arr = []
acc = 0
for i in range(K):
    arr.append(list(map(int, input().split()))[1:])
results = map(lambda x: sum(i**2 for i in x)%M, product(*arr))
print(max(results))
