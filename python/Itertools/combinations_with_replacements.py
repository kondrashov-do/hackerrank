from itertools import combinations_with_replacement
s, k = input().split()
print('\n'.join([(''.join(item)) for item in combinations_with_replacement(sorted(s), int(k))]))