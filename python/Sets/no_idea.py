n, m = map(int, input().split())
mood_input = [int(c) for c in input().split()]
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for i in range(len(mood_input)):
    if mood_input[i] in set_a:
        happiness += 1
    if mood_input[i] in set_b:
        happiness -= 1
print(happiness)