list1 = list(map(int, input("Enter the list elements seperated by spaces: ").split()))

def sum(list):
    sumlist = 0
    for i in range(len(list)):
        sumlist = sumlist + int(list[i])
    
    return sumlist

print(sum(list1))