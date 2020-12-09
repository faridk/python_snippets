from random import randint

def swap_vars(a=1, b=2):
    a = a + b  # 3 = 1 + 2
    b = a - b  # 1 = 3 - 2
    a = a - b  # 2 = 3 - 1
    return a, b

for i in range(10):
    a = randint(0, 100)
    b = randint(0, 100)
    print("Before:", (a, b))
    print("After:", swap_vars(a, b))
    print()
