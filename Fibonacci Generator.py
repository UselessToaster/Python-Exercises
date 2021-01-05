### generates a specified number of integers in the Fibonacci sequence ###

numbers = int(input("How many Fibonacci numbers do you want? "))
def Fibonacci_generator(add):
    fib = [1, add]
    for _ in range(numbers):
        add += fib[-2]
        fib.append(add)
        if len(fib) == numbers:
            break
    print (fib)
Fibonacci_generator(1)


