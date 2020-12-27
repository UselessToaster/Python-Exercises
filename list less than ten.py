# simple code that denotates what numbers in a given list 
# are less than a number chose by the user

import time

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("I have a list:")
time.sleep(2)

print(a)
time.sleep(2)

print("If you give me a number, I will tell you the numbers in my list that are less than the number you give me")
time.sleep(3)

print("Enter the number below:")
user = int(input())

print([aa for aa in a if aa < user])

# cheat sheet so i remember the syntax for this ^^:
    # output = aa
    # item = aa
    # list = a
    # filter = aa < 5
