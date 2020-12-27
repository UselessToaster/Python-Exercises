#<import time> to simulate a thinking/conversational AI
import time

#this set of code tells you if a number is divisible by 4 or 2
#if it isnt, it will say it's odd


print("Give me a number please!")
num = int(input())

if (num % 2 == 0):
    if (num % 4 == 0):
        print ("{} is divisible by 4 and 2".format(num))
    else:
        print("{} is even but not divisible by 4".format(num))
else:
    print("{} is an odd number and thus cannont be divided by 2 or 4".format(num))
   

#this functions the same as the first set of code 
#but uses user input to create more flexibility for application
print("If you give me two numbers I will tell you if the second divides evenly into the first!")
time.sleep(3)

print("First number please!")
num = int(input())

print("Second number please!")
check = int(input())

#i added theis just for fun lol
print("computing...")
time.sleep(3)

#same modulus function as before, just with different variables
if (num % check ==0):
    print("{} is divisible by {}".format(num, check))
else:
    print("{} is not divisible by {}".format(num, check))
    
#if there are ways to improve my code please let me know!
#i know this is just a simple application,
#but if i can apply a concept in a simple environment,
#then i can do it in a more complex environment.
