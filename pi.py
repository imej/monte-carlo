import random

def get_random_xy():
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    return (x, y)

def is_in_circle(x, y):
    return x * x + y * y < 1

def get_pi():
    in_circle_count = 0
    total_count = 100000000

    for i in range(total_count):
        (x, y) = get_random_xy()
        if is_in_circle(x, y):
            in_circle_count = in_circle_count + 1

    print(f'PI is: {4 * in_circle_count / total_count}')

get_pi()
# print(get_random_xy())
