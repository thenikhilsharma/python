def push(input, stack):             # function to enter an element
    stack.append(input)

def pop(stack):                     # function to remove an element
    stack.pop(length(stack)-1)

def peek(stack):                    # function to display the element
    print(stack)

def length(stack):
    lenStack = len(stack)           # length of stack
    return lenStack

def flowCheck(stack):
    if length(stack) == 0:          # assigning the value of under flow
        underFLOW = 1
        print("Stack is underflow")
    else:
        underFLOW = 0
        return False