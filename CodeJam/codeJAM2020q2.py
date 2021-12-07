# Python program to find the balanced 
# parentheses using the given number
# Function to find the balanced 
# parentheses using the given number 
def balance(m):
# Making the list of the 
 # given number 
 m = [int(i) for i in m]
# Empty list to store the 
 # parentheses 
 n = [] 
 
 # Iterating through the 
 # digits of the number 
 for i in m: 
  
  # Calculating the difference between 
  # opening and closing braces for the 
  # digit 
  if (n.count('(')-n.count(')'))<= i:
# If the next digit is greater, 
   # then open the brackets 
   while (n.count('(')-n.count(')')) != i: 
    n.append('(')   
   n.append(i)  
   
  # Similarly, find the difference 
  # between opening and closing braces 
  elif (n.count('(')-n.count(')'))>i:
# If the next digit is smaller, 
   # then close the brackets 
   while (n.count('(')-n.count(')'))!= i: 
    n.append(')') 
   n.append(i) 
   
 # Finally, close the remaining brackets 
 while (n.count('(')-n.count(')'))!= 0: 
  n.append(')') 
 
 # Returning the string 
 return ''.join(map(str, n)) 
 
# Driver code 
if __name__ == "__main__": 
 
 N = 312
 
 print(balance(str(N)))