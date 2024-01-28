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
        #print(f"{func.__name__}({args}) = {result:.3f}")
        return f"{func.__name__}({args}) = {result:.3f}"
    return wrapper


@pretty_printer
def sin_printer(x):
    return math.sin(x)


@pretty_printer
def cos_printer(x):
    return math.cos(x)


x = 1


def test_sin_printer_1():
    expected_result = "sin_printer(1) = 0.841"
    actual_result = sin_printer(x)
    if actual_result == expected_result:
        print("test_sin_printer_1: ok")
    else:
        print("test_sin_printer_1: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_cos_printer_1():
    expected_result = "cos_printer(1) = 0.540"
    actual_result = cos_printer(x)
    if actual_result == expected_result:
        print("test_cos_printer_1: ok")
    else:
        print("test_cos_printer_1: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_name_func_sin():
    expected_result = "sin_printer"
    actual_result = sin_printer.__name__
    if expected_result == actual_result:
        print("test_name_func_sin: ok")
    else:
        print("test_name_func_sin: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_name_func_cos():
    expected_result = "cos_printer"
    actual_result = cos_printer.__name__
    if expected_result == actual_result:
        print("test_name_func_cos: ok")
    else:
        print("test_name_func_cos: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_len_str_22():
    expected_result = 22  # cos_printer(1) = 0.540
    actual_result = len(sin_printer(x))
    if actual_result == expected_result:
        print("test_len_str_22: ok")
    else:
        print("test_len_str_22: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


if __name__ == "__main__":
    test_sin_printer_1()
    test_cos_printer_1()
    test_name_func_sin()
    test_name_func_cos()
    test_len_str_22()
