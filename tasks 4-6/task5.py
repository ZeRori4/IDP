"""
Написать декоратор для математической функции, 
который красиво печатает результат её выполнения, 
3 знака после запятой: 
@pretty_printer 
def sin(x): 
    return math.sin(x) 
sin(0) 
>> sin(0) = 0.000 

декоратор должен писать название функции
cos(0)
>> cos(0) = 1.000
"""

from functools import wraps
import math

def pretty_printer(func):
    @wraps(func)
    def wrapper(args):
        result = func(args)
        return "{}({}) = {:.3f}".format(func.__name__, args, result)
    return wrapper


def test_name_func_sin():
    @pretty_printer
    def sin_printer(x):
        return math.sin(x)
    expected_result = "sin_printer"
    actual_result = sin_printer.__name__
    if expected_result == actual_result:
        print("test_name_func_sin: ok")
    else:
        print("test_name_func_sin: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_check_three_zeros():
    x = 0
    @pretty_printer
    def sin_printer(x):
        return math.sin(x)
    expected_result = True  # sin_printer(0) = 0.000
    actual_result = sin_printer(x).endswith("000")
    if expected_result == actual_result:
        print("test_check_three_zeros: ok")
    else:
        print("test_check_three_zeros: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_len_num_float_point():
    @pretty_printer
    def cos_printer(x):
        return math.cos(x)
    expected_result = 3
    actual_result = len('{:.3f}'.format(
        float(cos_printer(0).split('= ')[-1])
    ).split('.')[-1])
    if actual_result == expected_result:
        print("test_len_num_float_point: ok")
    else:
        print("test_len_num_float_point: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_sin_printer_1():
    x = 1
    @pretty_printer
    def sin_printer(x):
        return math.sin(x)
    expected_result = "sin_printer(1) = 0.841"
    actual_result = sin_printer(x)
    if actual_result == expected_result:
        print("test_sin_printer_1: ok")
    else:
        print("test_sin_printer_1: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_isinstance_float():
    @pretty_printer
    def cos_printer(x):
        return math.cos(x)
    expected_result = '{:.3f}'.format(float(cos_printer(1).split('= ')[-1]))
    actual_result = cos_printer(1).split('= ')[-1]
    if actual_result == expected_result:
        print("test_isinstance_float: ok")
    else:
        print("test_isinstance_float: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


if __name__ == "__main__":
    test_name_func_sin()
    test_check_three_zeros()
    test_len_num_float_point()
    test_sin_printer_1()
    test_isinstance_float()
