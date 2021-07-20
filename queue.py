def underFlow(queue): #function to print if the queue is empty
    if underFLOW == 1:
        print("queue is underflow")
    else:
        return False

def push(input): #function to enter an element
    queue.insert(0, input)

def pop(queue): #function to remove an element
    queue.pop(lenqueue-1)

def peek():    #function to display the element
    print(queue)

queue = [1,2,3,4,5,6,17]    #specifying the queue
lenqueue = len(queue)   #length of queue

peek()  #calling peek function

if lenqueue == 0:   #assigning the value of under flow
    underFLOW = 1
else:
    underFLOW = 0

Input = input("Command: ")  #input from user to perform further function

if Input == "pop":  #checking the user input for pop
    if underFLOW == 1:  #checking for underflow
        print("queue is Empty")
    else:
        pop(queue)  #calling pop function

elif Input == "push":   #checking for user input for push
    pushValue = int(input("Enter a value to push: "))   #storing user input for pushh function
    push(pushValue)    #calling push function

elif Input == "peek":   #checkin user input for peek
    peek(queue)

else:   #checking user input for any other input
    pass

peek()