#MARBLE

vowels = ['a','e','i','o','u']

def cost(a, b):
    if (a == b):
        return 0
    isVowel = [True if a in vowels else False, True if b in vowels else False]
    if (isVowel[0] == isVowel[1]): return 2
    return 1

def extra(A):
    possibleAns = 1000000
    for i in range(26):
        temp = chr(97+i)
        sample = A
        countA = 0
        for j in range(len(sample)):
            x, y = sample[j]
            if (x == '?'): x = temp
            if (y == '?'): y = temp
            countA += cost(x, y)
        
        possibleAns = min(possibleAns, countA)
    return possibleAns

for _ in range(int(input())):
    N = int(input())
    S = input()
    P = input()

    count = 0
    A = []
    for i in range(N):
        if (S[i] == '?' and P[i] == '?'): continue
        if (S[i] == '?' or P[i] == '?'): A.append([S[i],P[i]])
        else: count += cost(S[i],P[i])
    count += extra(A)

    print(count)