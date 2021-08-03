# # def f():
# #     # return 'abc'
# #     # return 10
# #     # return [1, 2, 3]
# #     return 1, 2, 3
# #
# #
# # # result = f()
# # # print(result, type(result))
# #
# # a, b, c = f()
# # print(a, type(a))
# # print(b, type(b))
# # print(c, type(c))
# # result = f()
# # a = result[0]
# # b = result[1]
# # c = result[2]
#
# def f(n):
#     if n == 0:
#         return 0, 0, 0
#
#     total_sum, even_sum, odd_sum = f(n - 1)
#     total_sum += n
#     if n % 2 == 0:
#         even_sum += n
#     else:
#         odd_sum += n
#
#     return total_sum, even_sum, odd_sum
#
#
# # print(f(5))
# a, b, c = f(5)  # a, b, c = 15, 6, 9
# print('total_sum =', a)
# print('even_sum =', b)
# print('odd_sum =', c)

def f(*args, **kwargs):
    s = 0

    list_args = list(args) + list(kwargs.values())

    for i in list_args:
        # if isinstance(i, int) or isinstance(i, float):
        if type(i) in [int, float]:
            s += i
        elif type(i) == list:
            s += f(*i)

    return s


print(f(1, 1, [1, 1, [1, 1, [1, 1, [1, 1]]]], a=1, b=1, c=True, d=[1, 1, [1, 1, [1, 1]]]))
