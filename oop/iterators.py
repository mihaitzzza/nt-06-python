# # 1, 1, 2, 3, 5, 8, 13, 21 ...
# # n = 10
#
# def get_fibonnaci(n):
#     prev_value = 0
#     current_value = 1
#     result = []
#
#     for i in range(n):
#         result.append(current_value)
#
#         aux_value = prev_value
#         prev_value = current_value
#         current_value = aux_value + current_value
#
#     return result
#
#
# if __name__ == '__main__':
#     numbers = get_fibonnaci(1000)
#     print('numbers', numbers)


class Fibonnaci:
    def __init__(self, n):
        self._n = n

    def __iter__(self):
        # init the sequence
        self._prev_value = 0
        self._current_value = 1
        self._index = 0
        return self

    def __next__(self):
        if self._index == self._n:
            raise StopIteration()

        self._index += 1

        aux = self._prev_value
        self._prev_value = self._current_value
        self._current_value += aux

        return self._prev_value


if __name__ == '__main__':
    iterator = iter(Fibonnaci(10))
    # print('iterator', iterator)
    # print('first element:', next(iterator))

    for number in iterator:
        print('number', number)
        if number == 3:
            break

    # do some other stuff ...
    print('do some other stuff ...', next(iterator))
    for number in iterator:
        print('number', number)
