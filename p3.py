T = int(input("Enter No. of test cases: "))
print("No. of test cases are: ", T)

y = 0

def compare (comList, comInt):
    for j in range (1, T+1):
        for y in range (N):
            k = comList[y]
            j = y-1
            while j>=0 and k<comList[j]:
                comList[j+1] = comList[j]
                j = j-1
                y=y+1
            else:
                comList[j+1] = k
    print("Case #",comInt,":",y)

for i in range (1, T+1):
    print("Test case", i)

    N = int(input("Enter no. of elements for test case: "))
    print("No. of elements for list are: ", N)

    p = i
    m = str(p)

    m = []
    m = [int(x) for x in input("Enter multiple value: ").split()]
    print("Number of list is: ", m)
    
    compare(m, i)