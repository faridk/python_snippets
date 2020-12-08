def decorator_demo():

    def decorator(func):
        def wrapped_func():
            print("before")
            func()
            print("after")
        return wrapped_func

    @decorator
    # @decorator is syntactic sugar for this:
    # hello_world = decorator(hello_world)
    def hello_world():
        print('Hello world')

    hello_world()


def decorator_demo_with_arguments():

    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print("before")
            func(*args, **kwargs)
            print("after")
        return wrapped_func

    @decorator
    def add(a, b):
        print(f'Sum:{a + b}')

    add(1, 2)


# python.org/dev/peps/pep-0232
def function_attribute_decorator_demo():
    from datetime import datetime

    def exec_time_decorator(func):
        def wrapped_func(*args, **kwargs):
            start_time = datetime.now()
            ret_val = func(*args, **kwargs)
            end_time = datetime.now()

            # this is NOT a variable, this is a function attribute
            wrapped_func.time = end_time - start_time

            return ret_val

        return wrapped_func

    @exec_time_decorator
    def sum_up_to(num):
        sum = 0
        for i in range(num):
            sum += i
        return sum

    for pow in range(10):
        print(sum_up_to(10**pow))
        print("Time taken:", sum_up_to.time)


# decorator_demo()
# decorator_demo_with_arguments()
function_attribute_decorator_demo()