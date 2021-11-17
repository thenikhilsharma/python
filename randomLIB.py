import random   #imports module

array = [1,2,3,4,5,6]
print(random.choice(array)) #randomly choose any value from given array

random.seed(5)  #this is seeding value
print(random.random())
print(random.random())  #output of prg will alway same for a given input
#hence can't be used for encryption

r1 = random.randint(5, 15)  #generate a random value between 5 and 15
print("Random number between blah %s" % (r1))

r2 = random.randint(-10, -2)
print("Random no. between blah is %s" % (r2))

#print(random()) #prints random item

print(random.choice(array))

string = "geeks"
print(random.choice(string))    #prints random item from string

tuple = (1,2,3,4,5)
print(random.choice(tuple))

random.shuffle(array)   #shuffle array
print("After shuffling :")
print(array)

print(random.uniform(5,6))     #prints a floating value between 5, 6 both inclusive

#print(random.randrange[0:10:1])