#gives the factors of a chosen number from 1-100 

print("Pick a number, any number! :)")

x = int(input())
num_list = range(1, 101)
 
print("These are the divisors of {}: ".format(x), [num for num in num_list if x % num == 0])
