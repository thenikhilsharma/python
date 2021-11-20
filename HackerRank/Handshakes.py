t = int(input())

def combi(n):
    output = 0
    for j in range(n-1, 0, -1):
        output = output + j
    print(output)

for i in range(t):
    n = int(input())
    combi(n)