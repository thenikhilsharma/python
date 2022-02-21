import sys, math

sys.stdout = open('D:\\git repository\\thenikhilsharma_python\\CP\\output.txt', 'w')
sys.stdin = open('D:\\git repository\\thenikhilsharma_python\\CP\\input.txt', 'r')

for t in range(1, int(input())+1):
    n = int(input())
    citations = list(map(int, input().split()))