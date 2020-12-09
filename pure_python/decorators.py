def decorator_demo():

    def hello_world_decorator(func):
        def wrapper():
            print("before")
            func()
            print("after")
        return wrapper

    @hello_world_decorator
    # above statement is syntactic sugar for:
    # hello_world = decorator(hello_world)
    def hello_world():
        print('Hello world')

    hello_world()


def two_decorators_demo():
    def decorator_1(func):
        def wrapper():
            print("decorator 1")
            func()
        return wrapper

    def decorator_2(func):
        def wrapper():
            print("decorator 2")
            func()
        return wrapper

    @decorator_1
    @decorator_2
    # above statement is syntactic sugar for:
    # hello_world = decorator_1(decorator_2(hello_world))
    def hello_world():
        print('Hello world')

    hello_world()

def decorator_demo_with_arguments():

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("before")
            func(*args, **kwargs)
            print("after")
        return wrapper

    @decorator
    def add(a, b):
        print(f'Sum:{a + b}')

    add(1, 2)


def decorator_factory_demo():

    def decorator_factory(factory_arg):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("before", factory_arg)
                func(*args, **kwargs)
                print("after", factory_arg)
            return wrapper
        return decorator

    @decorator_factory("sum function")
    # above statement is syntactic sugar for:
    # add = decorator_factory("sum function")(add)
    # or:
    # decorator = decorator_factory("sum function")
    # add = decorator(add)
    def add(a, b):
        print(f'Sum:{a + b}')

    add(1, 2)


# python.org/dev/peps/pep-0232
def function_attribute_decorator_demo():
    from datetime import datetime

    def exec_time_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            ret_val = func(*args, **kwargs)
            end_time = datetime.now()

            # this is NOT a variable, this is a function attribute
            wrapper.time = end_time - start_time

            return ret_val

        return wrapper

    @exec_time_decorator
    def sum_up_to(num):
        sum = 0
        for i in range(num):
            sum += i
        return sum

    for power in range(10):
        print(sum_up_to(10**power))
        print("Time taken:", sum_up_to.time)


# decorator_demo()
# two_decorators_demo()
# decorator_demo_with_arguments()
# decorator_factory_demo()
function_attribute_decorator_demo()