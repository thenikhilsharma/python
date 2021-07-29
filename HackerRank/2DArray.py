# FILE IS CREATED BY TECH NICKK (YOUTUBE CHANNEL)
# Date - 27/07/2021

def hourglass(stack):                           # function to make hourglass
    arr = []                                    # creating an empty array "arr" to store hour glass data

    for i in range(n-2):                          # loop to traverse in rows
        for j in range(n-2):                      # loop to traverse in column
            arr.append(stack[i][j:j+3])           # enter 3 values to upper hour glass
            arr.append(stack[i+1][j+1])           # enter 1 value to middle of hour glass
            arr.append(stack[i+2][j:j+3])         # enter 3 values to lower hour glass

    #print("final array", arr)

    k = 0                                         # initialize variable k
    y = ((n-2) * (n-2)) * 3                       # calculate value for y
    maxlist=[]                                    # create an empty array "maxlist" to store sum of every hour glass

    while k < y:                                  # loop for summation
        z = sum(arr[k])+arr[k+1]+sum(arr[k+2])    # calculate sum of k hour glass
        maxlist.append(z)                         # insert sum value of hour glass to "maxlist" array
        k = k+3
    print(max(maxlist))                           # print max value of list maxlist

matrix = []                                       # creates an empty array for data input

n = int(input("Enter no of Rows/Column: "))       # takes input for no. of rows

for i in range (n):                               # loop for input
    row = list(map(int, input().split()))         # row input
    matrix.append(row)                            # append row input to new array

hourglass(matrix)                                 # calls function hour glass