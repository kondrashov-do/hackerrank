input()
set_a = set(map(int, input().split()))
for i in range(int(input())):
    in_operation = input().split()
    set_b = set(map(int, input().split()))
    eval('set_a.{0}({1})'.format(in_operation[0], set_b))
print(sum(set_a))