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
        print(f"{func.__name__}({args}) = {result:.3f}")
        return result
    return wrapper

@pretty_printer
def sin(x):
    return math.sin(x)

@pretty_printer
def cos(x):
    return math.cos(x)

print(sin(0))
print(cos(0))


def test_round_float(x):
    s = sin(x)
    if sin(x) == round(s, 3):
        print("s округлено до 3 знаков после запятой")
    else:
        print("s не округлено до 3 знаков после запятой")


def test_name_func_sin():
    if sin.__name__ == "sin":
        print(f"Имя функции {sin.__name__ } = sin")
    else:
        print(f"Имя функции {sin.__name__ } != sin")


def test_name_func_cos():
    if cos.__name__ == "sin":
        print(f"Имя функции {cos.__name__ } = cos")
    else:
        print(f"Имя функции {cos.__name__ } != cos")

if __name__ == "__main__":
    test_round_float(8)
    test_name_func_sin()
    test_name_func_cos()