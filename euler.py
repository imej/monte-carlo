'''
Select numbers between 0 and 1 randomly until sum > 1
The expected # of selections needed is equal to e (2.7182818).
'''
import random

tries = 100000
total_selection = 0

for i in range(tries):
    sum = 0
    selection = 0
    while sum < 1:
       r = random.random()
       sum = sum + r
       selection = selection + 1

    total_selection += selection

print(f"e: 2.7182818, and we got: {total_selection/tries}")
