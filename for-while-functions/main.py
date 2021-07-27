# # user_input = input('give me a number: ')
# # print('user_input', user_input, type(user_input))
# # user_input = int(user_input)
# # print('user inpiut from keyboard =', user_input, type(user_input))
#
# user_input = input('give me a number: ')
#
# try:
#     user_input = int(user_input)  # invalid literal for int() with base 10: 'abc123'
#     # print(another_variable)  # invalid literal for int() with base 10: 'abc123'
#     # print([][6])
# except ValueError as e:
#     print('Value Error', e)
# except NameError as e:
#     print('Name Error:', e)
# except IndexError as e:
#     print('Index Error:', e)
# else:  # this branch is not mandatory
#     print('THIS CODE IS RUN IF EVERYTHING IN TRY SUCCEED!')
# finally:  # this branch is not mandatory
#     print('THIS CODE IS RUN WHATEVER THE RESULT IN TRY IS!')
#
# print(user_input, type(user_input))

# user_input = None
#
# while user_input is None or type(user_input) is not int:
#     user_input = input('give me a number: ')
#
#     try:
#         user_input = int(user_input)
#     except ValueError:
#         print('Input is not an int. Try again!')

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = list(range(0, 10, 2))
# print(range(0, 10, 2), type(range(0, 10, 2)))

# for element in my_list:
#     print(element)

# for element in range(0, 10, 2):
#     print(element)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)

# my_list = list(range(1, 101))
# first_number = None
#
# for element in my_list:
#     print('iteration #')
#     if element % 5 == 0:
#         first_number = element
#         break
#
# print('END OF PROGRAM!', first_number)

# my_list = list(range(1, 101))
# index = 0
#
# while index < len(my_list):
#     print(my_list[index])
#     index += 1


# my_list = list(range(1, 101))
# first_number = None
# founded_after_iterations_no = 0
#
# for index, element in enumerate(my_list):
#     print('iteration #', index)
#     if element % 5 == 0:
#         first_number = element
#         founded_after_iterations_no = index + 1
#         break
#
# print('END OF PROGRAM!', first_number, founded_after_iterations_no)

# my_list = list(range(1, 101))
#
# for element in my_list:
#     if element % 2 == 0:
#         print('number', element, 'is even')
#         continue
#
#     print('number', element, 'is odd')
#
# print('END OF PROGRAM!')

# def my_first_function():
#     print('this is my first function!')
#     return [1, 2, 3]
#
#
# result_from_function = my_first_function()
# print('result_from_function', result_from_function)

# def my_sum(nr_1, nr_2, nr_3):
#     return nr_1 + nr_2 + nr_3
# def check_numbers(nr_1, nr_2):
#     return nr_1 < nr_2

# print('5 < 7', check_numbers(5, 7))
# print('5 < 7', check_numbers(nr_1=5))


# def my_result(nr_1, nr_2, operation_type='+', another_key_value_param=100):
#     print('operation_type', operation_type)
#     print('another_key_value_param', another_key_value_param)
#
#     if operation_type == '+':
#         return nr_1 + nr_2
#     else:
#         return nr_1 * nr_2
#
#
# print(my_result(5, 7, another_key_value_param=200))

# def my_function(a, b, *args, ka=0, kb=0, **kwargs):
#     print('a', a)
#     print('b', b)
#     print('args', args)
#     print('ka', ka)
#     print('kb', kb)
#     print('kwargs', kwargs)
#
#
# my_function(1, 2, 3, 4, 5, 6, 7, 8, ka=3, kb=4, kc=5, kd=6)


# def my_sum(a, b, c):
#     return a + b + c
#
#
# def multiply_sum(multiply_by, *args):
#     return multiply_by * my_sum(*args)
#
#
# print(my_sum(5, 7, 2))
# print(multiply_sum(5, 4, 2, 2))

# def my_function(a=0, b=1, c=2):
#     print(a, b, c)
#
#
# my_dict = {'a': 10, 'b': 20, 'c': 30}
# my_function(**my_dict)


# def recursive_sum(n):
#     if n == 0:
#         return 0
#
#     return n + recursive_sum(n - 1)
#
#
# print(recursive_sum(5))


l = [1, 2, 3]


def f():
    global l
    l.append(4)


print(l)
f()
print(l)
