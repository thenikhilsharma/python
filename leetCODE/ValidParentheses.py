def push(stack, input):             # function to enter an element
    stack.append(input)
def pull(stack):                     # function to remove an element
    stack.pop(length(stack)-1)
def peek(stack):                    # function to display the element
    print(stack)
def length(stack):
    return len(stack)           # length of stack
def flowCheck(stack):
    if len(stack) <= 0:          # assigning the value of under flow
        underFLOW = 1
        print("Stack is underflow")
    else:
        underFLOW = 0
        return False

inp = input()
arr = []

for i in range(len(inp)):
    if inp[i] == '(' or inp[i] == '[' or inp[i] == '{':
        push(arr,inp[i])
    else:
        a = arr.pop()

print(arr)