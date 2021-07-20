def underFlow(stack): #function to print if the stack is empty
    if underFLOW == 1:
        print("Stack is underflow")
    else:
        return False

def push(input): #function to enter an element
    stack.append(input)

def pop(stack): #function to remove an element
    stack.pop(lenStack-1)

def peek():    #function to display the element
    print(stack)

stack = [1,2,3,4,5,6,17]    #specifying the stack
lenStack = len(stack)   #length of stack

peek()  #calling peek function

if lenStack == 0:   #assigning the value of under flow
    underFLOW = 1
else:
    underFLOW = 0

Input = input("Command: ")  #input from user to perform further function

if Input == "pop":  #checking the user input for pop
    if underFLOW == 1:  #checking for underflow
        print("Stack is Empty")
    else:
        pop(stack)  #calling pop function

elif Input == "push":   #checking for user input for push
    pushValue = int(input("Enter a value to push: "))   #storing user input for pushh function
    push(pushValue)    #calling push function

elif Input == "peek":   #checkin user input for peek
    peek(stack)

else:   #checking user input for any other input
    pass

peek()