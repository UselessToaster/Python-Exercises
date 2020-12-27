### determines the even numbers in a randomly generated list of numbers ###

import random

# creates the random list
o = random.randint(0, 51)
rl = random.sample(range(0, 101), o)

#prints the list and the even numbers in the lsit
print ("List: ", rl) 
print("Even numbers in list: ", [n for n in rl if n % 2 == 0])

