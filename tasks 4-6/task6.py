"""
Написать функцию, которая распрямляет список.
Список [1, [2, 3], [[[[4]]]], [5, [6, [7, [8]]]], 9, [10]] 
-> 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
"""


def straightened_list(original_list):
    result = []
    for element in original_list:
        if isinstance(element, list):
            result.extend(straightened_list(element))
        else:
            result.append(element)
    return result


original_list = [1, [2, 3], [[[[4]]]], [5, [6, [7, [8]]]], 9, [10]]
output_list = straightened_list(original_list)
print(output_list)


def test_empty_report():
    if not original_list:
        print("test_empty_report: ok")
    else:
        print("test_empty_report: fail")


def test_base_report():
    if output_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("test_base_report: ok")
    else:
        print("test_base_report: fail")


def test_isinstance_output_list():
    if isinstance(output_list, list):
        print("test_isinstance_output_list: ok")
    else:
        print("test_isinstance_output_list: fail")

def test_isinstance_original_list():
    if isinstance(original_list, list):
        print("test_isinstance_original_list: ok")
    else:
        print("test_isinstance_original_list: fail")


def test_recursion():
    if list in output_list: # TODO
        print("test_recursion: ok")
    else:
        print("test_recursion: fail")



if __name__ == "__main__":
    test_empty_report()
    test_base_report()
    test_isinstance_output_list()
    test_isinstance_original_list()
    test_recursion()
    straightened_list(original_list)