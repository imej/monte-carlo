'''
In a group of 23 people, the probability of a shared birthday exceeds 50%.
'''
import random

def get_birthday():
    return round(random.random() * 365)

def one_group():
    birthdays = []
    for i in range(23):
        bd = get_birthday()
        try:
            birthdays.index(bd)
        except:
            birthdays.append(bd)
        else:
            return 1

    return 0

tries = 100000
shared_count = 0

for x in range(tries):
    shared_count += one_group()

print(f'In a group of 23 people, the probability of a shared birthday is {round(shared_count/tries * 100)}')
