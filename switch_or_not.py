'''
Suppose you're on a game show, and you're given the choice of three doors:
Behind one door is a valuable prize, behind the others, goats. You pick a
door, say No.1, and the host, how knows what's behind the doors, opens another
door, say No.3, which has a goat. He then says to you, "Do you want to pick
door No.2?" Is it to your advantage to switch your choice?
'''
import random

def game():
    prize = random.randint(1, 3)

    me = random.randint(1, 3)

    if me != prize:
        return 1

    return 0

tries = 1000000
win = 0
for i in range(tries):
    win += game()

print(f'My chance to win is {win/tries * 100} if I switch')
