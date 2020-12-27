print("pick a number, any number :)")
x = int(input())
num_list = range(1, 101)
print("these are the divisors of {}: ".format(x), [num for num in num_list if x % num == 0])
  
  