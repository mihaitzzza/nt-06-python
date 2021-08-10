# from decorators import my_sum  #, pow_decorator
from decorators import my_sum, pow_decorator_with_parameters, time_decorator

if __name__ == '__main__':
    # print(my_sum(2, 7))
    # my_decorated_function = pow_decorator(my_sum)
    # print('my_decorated_function', my_decorated_function)
    # print('my_decorated_function', my_decorated_function(2, 6))
    # print(my_sum(2, 3))

    # print(my_sum(2, 3))
    # print(my_sum.__wrapped__(2, 3))
    # print(my_sum.__name__)
    # print(my_sum.__doc__)

    # print(my_sum(2, 3))
    # my_decorated_function_pow_4 = pow_decorator_with_parameters(4)(my_sum)
    # print(my_decorated_function_pow_4(2, 3))
    #
    # my_decorated_function_pow_2 = pow_decorator_with_parameters(2)(my_sum)
    # print(my_decorated_function_pow_2(2, 3))

    my_decorated_function = time_decorator(my_sum)
    print(my_decorated_function(2, 3))
