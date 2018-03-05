from itertools import combinations
N = int(input())
l = input().split()
K = int(input())
number_of_combinations = 0
combinations_with_a = 0
for item in combinations(l, K):
    number_of_combinations += 1
    if 'a' in item: combinations_with_a += 1
print(combinations_with_a / number_of_combinations)