#unsolved

import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    n, k = map(int, input().split())
    default_program = list(map(int, input().split()))
    diff_arr, ans = [], 0

    for i in range(n):
        if i != n-1:
            diff_arr.append(default_program[i+1]-default_program[i])
    
    
    print('Case #%d: %d' % (tc+1, ans))