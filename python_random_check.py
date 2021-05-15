'''
Checks if the python random function will divide among 3 slots equally.
'''
import random

tries = 1000000
a = 0
b = 0
c = 0

for i in range(tries):
    x = round(random.random() * 3)
    if x == 1:
        a += 1
    elif x == 2:
        b += 1
    else:
        c += 1

print(a, b, c)
