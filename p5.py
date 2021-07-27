import stackModule as s

stack = [1,2,3]
s.peek(stack)

s.push(stack, 5)
s.peek(stack)

s.pop(stack)
s.peek(stack)

print(s.flowCheck(stack))

print(s.length(stack))