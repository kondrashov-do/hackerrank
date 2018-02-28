from itertools import groupby
s = input()
for item, grouper in groupby(s):
    print((len(list(grouper)), int(item)), end=' ')