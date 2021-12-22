#TYPING
#by Nikhil Sharma on 17th Dec

t = int(input())    #test case
for tc in range(t): #iteration in each test case
    n = int(input())    #no of words to enter
    wordList = []       #creating a list
    for i in range(n):  #iteration in each word
        word = input()  #input each word
        wordList.append(word)   #adding values to the list
    rightHand = ('j', 'k')      #assigning tuples for right hand
    leftHand = ('d', 'f')       #assigning tuples for left hand
    timeList = []               #initialising list for adding time for each word
    typedWords = []             #list for adding type words

    for i in wordList:          #loops to access each word
        time = 0                #initial time for each word = 0
        if i in typedWords:     #check if the word is already typed
            time = int(timeList[typedWords.index(i)] / 2)    #time will be half if it is already typed
            typedWords.append(i)    #add the typed word
        else:
            if i[0] in rightHand: currentHand = 'L' #ignore this logic
            elif i[0] in leftHand: currentHand = 'R' #this too
            for j in i:         #loop to access each letter
                if j in rightHand:  #check if the current letter is on right hand
                    if currentHand == 'R': time += 4  #check current hand
                    elif currentHand == 'L':
                        time += 2
                        currentHand = 'R'
                elif j in leftHand:
                    if currentHand == 'L': time += 4
                    elif currentHand == 'R':
                        time += 2
                        currentHand = 'L'
            typedWords.append(i)
        timeList.append(time)
    print(timeList, sum(timeList))