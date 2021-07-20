list1 = [47, 63, 22, 91]

def largestNo(list):
    for i in range (len(list1)):
        if list1[i] > list1[i+1]:
            list1[i] = list[i+1]