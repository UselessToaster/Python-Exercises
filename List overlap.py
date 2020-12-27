
#this code compares two lists 

import time
# two given lists from the exercise page:
# (i had to define them as sets to keep from double listing numbers)
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

print("Here are two predetermined lists:")
time.sleep(2)

print(a)
print(b)
time.sleep(3)

# loop to determine the elements list a has in common with b
print("Here are the numbers they have in common:")
time.sleep(2)
# the original way i figured out how to do it"
#   for n in a:
      # if n in b: 
          # print(n)
#   time.sleep(5)

# the most streamlined way i discovered i could do:
# (it also prints all in one line where the other prints all on different lines)
print([n for n in a if n in b])
# output = n
# item = n
# list = a
# filter = n in b <bool>
time.sleep(3)

#~~~~~~~~~#

# this set of code functions on the same principle as the first 
# except the lists are randomly generated 
import random

#random list 1
o = random.randint(0, 51)
RL1 = set(random.sample(range(0, 51), o))


#random list 2
m = random.randint(0, 51)
RL2 = set(random.sample(range(0, 51), m))

print("Here I have two randomly generated lists:")
time.sleep(2)

print(*[RL1])
print(*[RL2])
time.sleep(3)

print("Here are the numbers they have in common:")
time.sleep(2)
print([n for n in RL1 if n in RL2])

# original but longer notation
# for n in RL1:
    # if n in RL2: 
        # print(n)
