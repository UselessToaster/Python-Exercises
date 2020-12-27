# a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
# b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])


# for n in a:
    # if n in b: 
        # print(n)

import random
#random list 1
n = random.randint(0, 51)
RL1 = set(random.sample(range(0, 51), n))

#random list 2
m = random.randint(0, 51)
RL2 = set(random.sample(range(0, 51), n))

#print[(n for n in RL1 if n in RL2)]
for n in RL1:
    if n in RL2: 
        print(n)