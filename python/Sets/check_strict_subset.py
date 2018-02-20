A = set(input().split())
is_A_strict_superset = True
for i in range(int(input())):
    B = set(input().split())
    if not B.issubset(A) and len(A) > len(B):
        is_A_strict_superset = False
        break
print(is_A_strict_superset)