#AMR15A

n = int(input())
a = list(map(int, input().split()))

ready, notready = 0, 0
for i in a:
    if i % 2 == 0: ready += 1
    else: notready += 1

print('READY FOR BATTLE') if ready > notready else print('NOT READY')