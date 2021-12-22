class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):         #initialising
        self.head = None

    def addNode(self, newData): #add nodes at the end
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    
    def deleteNode(self, key):  #deletes node with value
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next

        temp = None
    
    def deleteIndexNode(self, position):    #deletes node at index
        if self.head == None:
            return 
        # Store head node
        temp = self.head
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return 
        # Find previous node of the node to be deleted
        for i in range(position -1 ):
            temp = temp.next
            if temp is None:
                break
        # If position is more than number of nodes
        if temp is None:
            return 
        if temp.next is None:
            return 
        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next
        # Unlink the node from linked list
        temp.next = None
        temp.next = next
    
    def deleteList(self):   #deletes whole linked list 
        # initialize the current node
        current = self.head
        while current:
            prev = current.next  # move next node
            # delete the current node
            del current.data
            # set current equals prev node
            current = prev
    
    def getCount(self):     #counts length of linked list
        temp = self.head # Initialise temp
        count = 0 # Initialise count
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count
    
    def search(self, x):    #search node with given value
        # Initialize current to head
        current = self.head
        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True # data found
            current = current.next
        return False # Data Not found
    
    def getNth(self, index):    #search node at given index
        current = self.head  # Initialise temp
        count = 0  # Index of current node
        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert(False)
        return 0

    def printLL(self):      #print whole linked list
        temp = self.head
        while temp:
            print(" %d" %(temp.data), end=''),
            temp = temp.next

rootNode = LL()
rootNode.addNode(7)
rootNode.addNode(1)
rootNode.addNode(11)
rootNode.addNode(9)
rootNode.addNode(10)
rootNode.addNode(12)
print('created ll is: ')
rootNode.printLL()
rootNode.deleteNode(11) #delete node with value
print('\n ll now is: ')
rootNode.printLL()
rootNode.deleteIndexNode(1)  #delete node at index
print('\n ll now is: ')
rootNode.printLL()