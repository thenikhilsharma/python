#SNAKEPROC
#by Nikhil Sharma on 17 dec 2021

t = int(input())
for tc in range(t):
    output = True
    n = int(input())
    string = input()
    snakeArray = []
    for i in range(len(string)):
        if string[i] == 'H' or string[i] == 'T': snakeArray.append(string[i])
        else: continue
    if snakeArray == []: output == True
    else:
        if snakeArray[0] == 'H' and snakeArray[len(snakeArray)-1] == 'T':
            for i in range(len(snakeArray)):
                if i != len(snakeArray) - 1:
                    if snakeArray[i] == 'H' and snakeArray[i+1] == 'T': continue
                    elif snakeArray[i] == 'T' and snakeArray[i+1] == 'H': continue
                    else: output = False
        else: output = False
    print("Valid") if output == True else print("Invalid")