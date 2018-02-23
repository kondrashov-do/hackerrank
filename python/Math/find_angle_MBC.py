from math import atan2, degrees
AB = int(input())
BC = int(input())
print(str(round(degrees(atan2(AB,BC))))+'°')