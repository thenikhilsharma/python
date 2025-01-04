import sys

sys.stdout = open('C:\\Users\\Nikita Sharma\\OneDrive\\Tài liệu\\codes\\python\\CP\\output.txt', 'w')
sys.stdin = open('C:\\Users\\Nikita Sharma\\OneDrive\\Tài liệu\\codes\\python\\CP\\input.txt', 'r')

for _ in range (int(input())):
    a = list(map(int, input().split()))
    