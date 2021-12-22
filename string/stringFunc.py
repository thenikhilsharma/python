string = input("Enter a string")    #string input
print(string)                       #

n = 1           #
string = str(n) #string conversion
print(string)   #

lst = ['a','b','c','d','e']     #
string = ''.join(lst)           #list to string
print(string)                   #

print(string.islower())         #true if lower case
print(string.upper())           #convert to upper case

print(string.isupper())         #true if upper case
print(string.lower())           #convert to lower case

#Manipulating String
x = "Bro"
y = "Sena"
z = x+y
print(z)

#replication
print(2*z)

#Membership Operators
if "B" in x:
    print("true")
else:
    print("False")

if "B" not in x:
    print("true")
else:
    print("False")

#Comparision
if x == y:
    print("true")
else:
    print("false")

#ending strip
#print the rest of the text else then labelled in lstrip
x = "the topper"
print(x.rstrip("er ps"))

y = "the topper        "
print(y.rstrip()) #remove empty spaces from end

#leading strip
#print the rest of the text else then labelled in lstrip
x = "the topper"
print(x.lstrip("p te h"))

y = "           the topper"
print(y.lstrip()) #remove empty spaces from start

#isspace
x = "     "
print(x.isspace())

#isdigit()
x = input("Enter any number")
print(x.isdigit())

#isalpha only alphabet
x = "theTopper"
print(x.isalpha())

#alphabet or number or combination
x = "theToppers12"
print(x.isalnum())

x = "python how is find character"
print(x.find("is"))
print(x.find("is",9,15)) #search from 9 to 15th character
#prints -1 on false

x = "python"
print(x.capitalize())

#Taking Part
x = "programming"
print(x[3:5:1])