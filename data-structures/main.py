# import copy
#
# # my_list = [1, -1, 10.10, -10.01, 3+3j, True, False, None, 'string 1', [1, 2, 3]]
# #          0   1   2        3 ......................................     9
# #                                                                      0  1  2
# #         -10  ..................................    -3      -2         -1
# # print(my_list, type(my_list))
# # print(my_list[0])
# # print(my_list[1])
# # print(my_list[2])
# # print(my_list[9])
# # print(my_list[9][0])
# # print(my_list[9][1])
# # print(my_list[9][2])
# # print(my_list[9][3])
# # print(my_list[-1])
# # print(my_list[-2])
# # print(my_list[-3])
# # print(my_list[-10])
# # print('list length =', len(my_list))
# # print(my_list[len(my_list) // 2 - 1])
#
# # slice => my_list[start_index:end_index:step]
# # print(my_list[1::])
# # print(my_list[1:9:])
# # print(my_list[1:9:2])
# # print(my_list[:5])
# # print(my_list[::-2])
# # print(my_list[-3::-1])
#
# # print(len('abc'))
# # print('abc'[0])
# # print('abc'[1])
# # print('abc'[2])
# # print('abc'[::-1])
#
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(5 in my_list)
# # print(15 in my_list)
# # print(5 not in my_list)
# # print(15 not in my_list)
# # print('are' in 'Ana are mere')
# # print(7 is 7)
# # print([1, 2, 3] is [1, 2, 3])
# # print([1, 2, 3] == [1, 2, 3])
# a = [1, 2, 3, ['a', 'b', 'c']]
# b = [1, 2, 3]
# # c = a.copy()  # shallow copy
# # c = a[:]  # shallow copy
# c = copy.deepcopy(a)
# # print(a is b)
# # print(a is c)
# print('a', a)
# a.append(4)  # a => [1, 2, 3, ['a', 'b', 'c'], 4]
# a[3].append('d')  # a => [1, 2, 3, ['a', 'b', 'c', 'd'], 4]
# # print('a', a)
# # print('b', b)
# # print('c', c)
# a[0] = 'abc'
# print(a)

# my_tuple = (1, 2, 'a', 'abc')
# print(my_tuple, type(my_tuple))
# print(my_tuple[0])
# print(my_tuple[1:2])

# # my_list = [1, 2, 3]
# my_tuple = ('a', 'b', 'c')
# print(id(my_tuple))
# # tuple_from_my_list = tuple(my_list)
# # print(tuple_from_my_list, type(tuple_from_my_list))
# list_from_my_tuple = list(my_tuple)
# # print(list_from_my_tuple, type(list_from_my_tuple))
# list_from_my_tuple.append('d')
# my_tuple = tuple(list_from_my_tuple)
# print(my_tuple, type(my_tuple))
# print(id(my_tuple))

# l = [1, 2, 3]
# t = tuple(l)
# print(l is t)
# l.append(4)
# print(t)

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
}
# print(my_dict, type(my_dict))
# print(my_dict['a'])
# print(my_dict['b'])
# print(my_dict['c'])
# print('a' in my_dict)
# print('d' in my_dict)
# print(my_dict['c'])
# # print(my_dict['d'])
# print(my_dict.get('d', 'd'))
# my_dict['d'] = 4
# print(my_dict.get('d', None))
# print(my_dict)
# my_dict_keys = my_dict.keys()  # get all keys from dictionary (object: dict_keys)
# my_dict_keys_list = list(my_dict_keys)
# print(my_dict_keys_list)
# # print('a' in my_dict_keys_list)
#
# my_dict_values = my_dict.values()  # get all values from dictionary (object: my_dict_values)
# my_dict_values_list = list(my_dict_values)
# # print(my_dict_values, type(my_dict_values))
# # print('my_dict_values_list', my_dict_values_list)
# # print(2 in my_dict_values_list)
# # print(5 in my_dict_values_list)
#
# my_dict_items = my_dict.items()  # get all items from dictionary (object: my_dict_items)
# my_dict_items_list = list(my_dict_items)
# print(my_dict_items_list)
#
# print('my_dict', my_dict)
# my_dict['d'] = 4
# print('my_dict', my_dict)
# # del my_dict['c']
# my_dict.pop('c')
# print('my_dict', my_dict)

# my_set = {1, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10}
# print(my_set, type(my_set))
# # my_set.pop()
# # my_set.remove(10)
# my_set.discard(10)
# print(my_set)

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6, 7, 8}
# print(set_1.intersection(set_2))

# set_1 = {1, 2, 3}
# set_2 = {2, 3}
# print(set_1.issuperset(set_2))
# print(set_2.issubset(set_1))

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6, 7, 8}
# print(set_1.union(set_2))
# print(set_1.difference(set_2))

# my_list = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7]
# my_list = list(set(my_list))
# print(my_list)

my_number = 3

if my_number % 2 == 0:
    print(f'Number {my_number} is even.')

    if my_number < 5:
        print(f'Number is lower then 5')
elif my_number < 5:
    print(f'Number {my_number} is lower then 5')
else:
    print(f'Number {my_number} is odd.')

print('end of program')
