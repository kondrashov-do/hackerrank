from cmath import polar, phase
from math import sqrt, pow
complex_num = complex(input())
#print(polar(complex_num))
#print(sqrt(pow(complex_num.real, 2) + pow(complex_num.imag, 2)))

print(abs(complex_num))
print(phase(complex_num))