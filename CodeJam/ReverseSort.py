#Qualification Round 2021 - Code Jam 2021
#Reversort

t = int(input())
for z in range(t):
    n = int(input())    #no of elements in input array
    arr = input()   #input array
    arr = arr.split()

    def ReverseSort(array):
        sortedArray = sorted(arr)
        cost = 0
        for i in range(len(array)):
            a = array.index(sortedArray[i])
            d = int(a)
            b = array[i]
            array[i] = array[a]
            array[a] = b
            j = d + 1
            c = i + 1
            diff = j-c
            cost = cost+diff+1
            if array == sortedArray:
                break
        print("Case #%s:"%(z+1),cost)

    ReverseSort(arr)