import time

# print("Give me a number please!")
# num = int(input())
# #even = (num % 2)

# if (num % 2 == 0):
    # if (num % 4 == 0):
        # print ("{} is divisible by 4 and 2".format(num))
    # else:
        # print("{} is even but not divisible by 4".format(num))
# else:
    # print("{} is an odd number and thus cannont be divided by 2 or 4".format(num))

print("If you give me two numbers i will tell you if the second divides evenly into the first!")
time.sleep(3)
print("first number please!")
num = int(input())
print("Second number please!")
check = int(input())
print("computing...")
time.sleep(3)
if (num % check ==0):
    print("{} is divisible by {}".format(num, check))
else:
    print("{} is not divisible by {}".format(num, check))
