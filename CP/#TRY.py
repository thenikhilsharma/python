import random as rm

symbols = '[]{}()<>,.:/;*-_+!@#$%^&*?'
numbers = '0123456789'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

all =  upper + lower + numbers + symbols
length = 16
password = ''.join(rm.sample(all, length))
print('Your password is :', password)