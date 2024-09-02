"""
Написать функцию, которая распрямляет список.
Список [1, [2, 3], [[[[4]]]], [5, [6, [7, [8]]]], 9, [10]] 
-> 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
"""


def flatten_list(original_list):
    result = []
    for element in original_list:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result


def test_empty_list():
    test_data = []
    expected_result = []
    actual_result = flatten_list(test_data)
    if actual_result == expected_result:
        print("test_empty_list: ok")
    else:
        print("test_empty_list: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_flat_list_len_1():
    test_data = [1]
    expected_result = [1]
    actual_result = flatten_list(test_data)
    if actual_result == expected_result:
        print("test_flat_list_len_1: ok")
    else:
        print("test_flat_list_len_1: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_flat_list_len_3():
    test_data = [1, 2, 3]
    expected_result = [1, 2, 3]
    actual_result = flatten_list(test_data)
    if actual_result == expected_result:
        print("test_flat_list_len_3: ok")
    else:
        print("test_flat_list_len_3: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_nested_list_level_1():
    test_data = [1, 2, [3]]
    expected_result = [1, 2, 3]
    actual_result = flatten_list(test_data)
    if actual_result == expected_result:
        print("test_nested_list_level_1: ok")
    else:
        print("test_nested_list_level_1: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


def test_nested_list_level_3():
    test_data = [1, 2, [3, [4, [5, 6, 7, 8, 9, 10]]]]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual_result = flatten_list(test_data)
    if actual_result == expected_result:
        print("test_nested_list_level_3: ok")
    else:
        print("test_nested_list_level_3: fail")
        print("Expected: {}, actual: {}".format(expected_result, actual_result))


if __name__ == "__main__":
    test_empty_list()
    test_flat_list_len_1()
    test_flat_list_len_3()
    test_nested_list_level_1()
    test_nested_list_level_3()
