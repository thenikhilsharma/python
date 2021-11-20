def flow(queue): #function to print if the queue is empty
    if length(queue) == 0:   #assigning the value of under flow
        return "queue is underflow"
    else:
        return False

def queue(queue, input): #function to enter an element
    queue.insert(0, input)

def dequeue(queue): #function to remove an element
    queue.pop(length(queue)-1)

def peek(queue):    #function to display the element
    print(queue)

def length(queue):
    lenqueue = len(queue)   #length of queue
    return lenqueue