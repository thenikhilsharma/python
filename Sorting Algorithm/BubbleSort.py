def Sort(arr):
    size = len(arr)  #find length of array

    for i in range (size):
        for j in range(size-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr