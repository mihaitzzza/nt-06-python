import time


def time_decorator(my_function):
    def wrapper(*args, **kwargs):
        start_time_in_ms = time.time() * 1000
        # print('start_time_in_ms', start_time_in_ms)

        result = my_function(*args, **kwargs)

        end_time_in_ms = time.time() * 1000
        # print('end_time_in_ms', end_time_in_ms)
        duration_time = end_time_in_ms - start_time_in_ms
        print('FUNCTION EXECUTION TIME:', duration_time)

        return result

    return wrapper
