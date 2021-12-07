#by Nikhil Sharma on 1DEC
#@ 9:11pm

import math as m

A = int(input())
B = int(input())
C = int(input())

discriminant = m.sqrt(B**2 - 4*A*C)
numerator1 = -B + discriminant
numerator2 = -B - discriminant
root1 = numerator1/2*A
root2 = numerator2/2*A
print(int(root1))
print(int(root2))