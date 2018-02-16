stamps_amount = int(input())
stamps = []
for i in range(stamps_amount):
    stamps.append(input())
print(len(set(stamps)))