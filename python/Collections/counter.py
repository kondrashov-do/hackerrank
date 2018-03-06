from collections import Counter
number_of_shoes = int(input())
sizes = list(map(int, input().split()))
count = Counter(sizes)
earned_money = 0
for i in range(int(input())):
    size, price = map(int, input().split())
    if count[size] > 0:
        earned_money += price
        count[size] -= 1
print(earned_money)
