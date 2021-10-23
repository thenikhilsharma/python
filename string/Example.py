
YourName = input("Input Your Name ") #Stores your name in the variable YourName

#deletes empty spaces from start and end
YourName.lstrip()
YourName.rstrip()

#isAlphabet & isNumber (Check whether all character are alphabet or digit)
if YourName.isalpha():
    print("All your text have characters")
elif YourName.isnum():
    print("All your text have numbers")
else:
    print("It contains mixed texts")

#Length Fuction
print("Number of letter in your name is ", len(YourName)) #Prints the total number of letters
Inp = int(input("Which Digit do u want to show ")) #Input which letter do u want to show
if Inp <= len(YourName):
    print("The", Inp, "Letter of your name is : ",YourName[Inp-1])
else:
    print("Enter a number less than", len(YourName))

#For Loop (for printing letters seperately)
approval = input("Do you want to print your name letters seperately. Y/N ")
if approval == "Y":
    for i in range(len(YourName)):
        print(YourName[i])
elif approval == "N":
    print("As your Wish")
else:
    print("Enter a valid input ")

#isLower & isUpper (Identifies whether your text is all small or capital)
if YourName.islower():
    print("Your Entered text is all in Lower Case")
elif YourName.isupper():
    print("Your Entered text is all in Upper Case")
else:
    print("Your Entered text is consist of all cases")

#Capitalization (Sentence Case)
case = input("Would you like to make all your text capital: Y/N ")
if case == "Y":
    print(YourName.capitalize())
elif case == "N":
    print("As your Wish")
else:
    print("Enter a valid input ")

#
