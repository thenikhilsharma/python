def binarySearch(arr, size, key):
    start = 0
    end = size-1

    mid = (start + end) / 2
    mid = int(mid)

    while start <= end:
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            start = mid+1
        elif key < arr[mid]:
            end = mid-1
        
        mid = (start + end) / 2
        mid = int(mid)

    return mid

arr = list(map(int, input("Input a sorted array: ").split()))
length = len(arr)
search = int(input("Element U want to search is: "))

index = binarySearch(arr, length, search)

print("index of", search,"is: ", index)