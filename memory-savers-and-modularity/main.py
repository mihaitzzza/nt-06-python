# print(dir(__builtins__))  # show all builtins from Python (built-in namespace)

# a = 10
#
#
# def my_sum(nr_1, nr_2):
#     global a
#
#     def print_sum():
#         v = 'this is v from local of print_sum'
#         print('enclosing function will return s =', s, v, a)
#
#     s = a + nr_1 + nr_2
#     print_sum()
#     return s
#
#
# print(my_sum(1, 2))


# my_var = 10
#
#
# def my_sum(nr_1, nr_2):
#     def print_sum():
#         # my_var = 'this is v from local of print_sum'
#         print('enclosing function will return s =', s, my_var)
#
#     # my_var = 20
#     s = my_var + nr_1 + nr_2
#     print_sum()
#     return s
#
#
# print(my_sum(1, 2))

# import my_module
# import my_module as tagged_module
# from my_module import *
# from my_module import my_sum, my_list as my_list_from_my_module
# import my_package.my_module as mfp
# from my_package import my_prod, my_list as l_from_package

# my_list = ['a', 'b', 'c']

# from itertools import zip_longest

if __name__ == '__main__':
    # print(__name__)
    #
    # a = 10
    # b = 20
    #
    # # print(my_module.my_sum(a, b))
    # # print(tagged_module.my_sum(a, b))
    # print(my_sum(a, b))
    # print(my_list)
    # print(my_list_from_my_module)
    #
    # # print(my_package.my_module.my_prod(a, b))
    # print(my_prod(a, b))
    # print(l_from_package)

    # my_lambda = lambda a, b: a + b
    # print(id(my_lambda))
    # print(my_lambda(5, 7))
    # print(id(my_lambda))
    # print(id(my_lambda))
    # print(id(my_lambda))
    # print(id(my_lambda))
    # print(id(my_lambda))
    # print(id(lambda a, b: a + b))
    # print(id(lambda a, b: a * b))
    # print(id(lambda a, b: a ** b))
    # print(id(lambda a, b: a - b))

    # l = [5, 2, 7]
    # l = sorted(l)
    # print(l)

    # def get_student_sort(student):
    #     grade = student.get('grade')
    #
    #     if grade is not None:
    #         return student['grade']
    #
    #     return 0.00

    students = [{
        'name': 'name1',
        'grade': 5.60
    }, {
        'name': 'name2',
        'grade': 3.50
    }, {
        'name': 'name3',
        'grade': 10.00
    }, {
        'name': 'name4',
    }]
    # sorted_students = sorted(students, key=get_student_sort, reverse=True)
    # sorted_students = sorted(students, key=lambda obj: obj.get('grade', 0.00), reverse=True)
    # print('students', students)
    # print('sorted_students', sorted_students)

    # a = [1, 2, 3]  # => [1 ** 1, 2 ** 2, 3 ** 3]
    # if obj % 2 == 0:
    #   return obj ** obj
    # else:
    #   return obj
    # a_map = list(map(lambda obj: obj ** obj if obj % 2 == 0 else obj, a))
    # print('a_map', a_map)

    # v = 20 if 4 % 2 != 0 else 100
    # print('--- v', v)

    # def update_student(student):
    #     grade = student.get('grade', 0.00)
    #
    #     return {
    #         **student,
    #         'grade': grade,
    #     }

    # students = list(
    #     map(update_student, students)
    # )
    # students = list(
    #     map(lambda student: {
    #         **student,
    #         'grade': student.get('grade', 0.00)
    #     }, students)
    # )
    # # print('students', students)
    #
    # promoted_students = list(filter(lambda student: student['grade'] > 5.0, students))
    # print('promoted_students', promoted_students)

    # a = [1, 2, 3]
    # b = ['a', 'b', 'c']
    # # r = [(1, 'a'), (2, 'b'), (3, 'c')]
    # c = [10, 20, 'abc', 50, 60, 70]
    # # r = list(zip(a, b, c))
    # # r = list(zip(a, c, b))
    # r = list(zip_longest(a, c, b, fillvalue=0))
    # print('r', r)

    # a = list(range(0, 100))
    # b = list(filter(lambda n: n % 2 == 0, a))
    # print('b', b)
    # c = list(map(lambda n: 0 if n % 5 == 0 else n, b))
    # print('c', c)
    # b = [n for n in a if n % 2 == 0]
    # print('b', b)
    # c = [0 if n % 5 == 0 else n for n in b]
    # print('c', c)
    # b = [0 if n % 5 == 0 else n for n in a if n % 2 == 0]
    # print('b', b)

    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    # d = dict(zip(a, b))
    # print('d', d)
    d = {
        k: v
        for k, v in zip(a, b)
    }
    print('d', d)
