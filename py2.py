# takes input from user and store it in val
val = input("Enter the amount of check")
val_list = []

# check the length of the value
length = len(val)

for i in range(length):
    val_list[i] = i
print(val_list)

val = int(val) # convert val string to integer

'''while (i <= 10):
    divisor = 10**length # check places of digit
    
ones_digit = val % divisor'''