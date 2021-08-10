from functools import wraps


def pow_decorator(my_function):
    @wraps(my_function)
    def wrapper(a, b):
        my_function_result = my_function(a, b)
        return my_function_result ** 2

    return wrapper


def pow_decorator_with_parameters(param):
    def pow_decorator(my_function):
        def wrapper(a, b):
            my_function_result = my_function(a, b)
            return my_function_result ** param

        return wrapper

    return pow_decorator
