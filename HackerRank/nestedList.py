n = int(input())
records = []

for i in range (n):
    name = input()
    score = float(input())
    records.append([name, score])

print (records)

second_highest = sorted(set([score for name, score in records]))[1]
print('\n'.join(sorted([name for name, score in records if score == second_highest])))