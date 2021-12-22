t = int(input())
for tc in range(t):
    n = int(input())
    s = input()
    arr = []
    for i in range(len(s)): arr.append(s[i])
    s = arr
    print(s)

    def winner(a, b):
        rule = [['R', 'P'], ['P', 'S'], ['S', 'R']]
        for i in range(3):
            if a != b:
                if [a, b] == rule[i]: return b
                if [b, a] == rule[i]: return a
            else: return b

    def iteration(x, y):
        if s.index(y) == len(s) - 1:
            w = winner(x, y)
            return w
        else:
            w = winner(x, y)
            return iteration(w, s[s.index(y)+1])

    for i in range(len(s)):
        if i != len(s) - 1:
            print(iteration(s[i], s[i+1]))