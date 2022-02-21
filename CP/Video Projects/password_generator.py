#by Tech Nickk YouTube Channel

#so this is password generator
import random as rm

symbols = "[]{}()!@#$%^&*"
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'

all = upper + lower + numbers + symbols
length = 9
password = ''.join(rm.sample(all, length))
print('the password is:', password)

#like and subscribe :)