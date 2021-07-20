n = int(input())

wordList = []
occList = []
duplicate = []

for i in range(n):
    word = input()
    wordList.append(word)
print(wordList)

length = len(wordList)

for j in range(n):
    occurence = wordList.count(wordList[j])
    if occurence > 1:
        for l in range (occurence):
            index = wordList.index(wordList[j])
            duplicate.append(index)
            print(duplicate)
            for m in range (len(duplicate)):
                wordList.remove(duplicate[m])

    occList.append(occurence)

print(n)

for k in range(length):
    print(occList[k], end="")