#Insertion Sort Module
#Functions - Sort()

def Sort(arr):
    size = len(arr)
    for i in range(1, size):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

    return arr