#Module for Selection Sort
#Functions - Sort()

def Sort(arr):
    size = len(arr)

    for i in range (size):
        k = arr[i]
        j = i-1
        while j>=0 and k<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        else:
            arr[j+1] = k

    return arr