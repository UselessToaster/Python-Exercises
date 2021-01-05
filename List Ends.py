### makes a new list of only the first and last elements of a randomly generated list ###

import random

def list_generator():
    n = random.randint(0,100)
    L1 = random.sample(range(0,101), n)
    print("Original list:", L1) 
    print("First and last numbers of list:", L1[0], L1[-1]) 
list_generator()