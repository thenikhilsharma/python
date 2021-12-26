import sys
import collections
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

c = collections.Counter()
print ('Initial :', c)

c.update('abcdaab')
print ('Sequence:', c)