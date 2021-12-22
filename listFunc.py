list1 = [] #empty list
list2 = [1, 2, 3, 5] #creating a list
print(list2) #printing a list
#adding elements
list2.append([6, 8]) #adds as a single element
print(list2)
list2.extend([7, 'more_example']) #adds as different elements
print(list2)
list2.insert(1, 'insert') #add element at i
print(list2)

#deleting elements
del list2[1] #delete element at index at 1
print(list2)
list2.remove('more_example') #remove element with value
print(list2)
list2.pop(1) #pop elements from list
print(list2)
list2.clear() #empty the list
print(list2)

#accessing elements
list2 = [1,2,3,'example',3.213]

for elements in list2: #access elements one by one
    print(elements)
print(list2) #access all elements
print(list2[3]) #access 3 index element
print(list2[0:2]) #access elements from index 0 to 1 exclude 2
print(list2[::-1]) #access elements in reverse

list2.clear()
list2 = [2,3,4,6,1]

#other function on list
print(len(list2)) #find length of list
print(list2.index(2)) #find index of the element that occurs first
print(list2.count(10)) #find count of the elements
print(sorted(list2)) #print sorted list but not change original
list2.sort(reverse=True) #sort original list
print(list2)

#list1, list2 = [123, 'xyz'], [456, 'abc']
#print(cmp(list1, list2))