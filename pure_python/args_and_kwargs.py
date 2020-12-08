# Single star unpacks a tuple or a string
# Works not only in function arguments, but also in lists
# e.g. [*(1, 2, 3)] or [*'Hello']
def list_args(*args):
    print("The following positional (unnamed) arguments were provided: ", end='')
    for arg in args:
        print(arg, end=', ')
    print("\b\b ")  # remove the trailing comma


def list_first_three_and_other_args(first, second, third, *others):
    print("The following positional (unnamed) arguments were provided: ", end='')
    print(first, end=', ')
    print(second, end=', ')
    print(third, end=', ')
    for other in others:
        print(other, end=', ')
    print("\b\b ")  # remove the trailing comma

# Double star unpacks a dictionary only into function arguments
def list_kwargs(**kwargs):
    print("The following keyword (named) arguments were provided: ")
    for kwarg_name, kwarg_value in kwargs.items():
        print(kwarg_name, kwarg_value)

def match_kwargs():
    def add_one_and_two(one, two):
        return one + two
    kwargs = {'two': 2, 'one': 1}
    print("One plus two is: ", add_one_and_two(**kwargs))

def list_args_and_kwargs(*args, **kwargs):
    list_args(*args)
    list_kwargs(**kwargs)


list_args(1, 2, 3, 4, 5)
list_first_three_and_other_args(1, 2, 3, 4, 5)
list_args_and_kwargs(1, 2, 3, fourth=4, fifth=5)
match_kwargs()

# TypeError: list_kwargs() takes 0 positional arguments but 3 were given
# list_kwargs(1, 2, 3, fourth=4, fifth=5)

# TypeError: list_args() got an unexpected keyword argument 'fourth'
# list_args(1, 2, 3, fourth=4, fifth=5)