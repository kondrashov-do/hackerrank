#import numpy as np
n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))
#print(np.average(x, weights=w))
"""
elementsSum = 0
weightsSum = 0
for i in range(n):
    elementsSum += x[i]*w[i]
    weightsSum += w[i]
print('{0:.1f}'.format(elementsSum/weightsSum))
"""
print(round((sum([i*j for i,j in zip(x, w)]))/sum(w), 1))
