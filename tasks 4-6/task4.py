"""
Есть словарик data = dict(user_1=dict(a=10, b=70), 
                        user_2=dict(a=12, b=70), 
                        user_3=dict(a=7, b=19), 
                        user_4=dict(a=12, b=19), 
                        user_5=dict(a=55, b=1)). 
Нужно вывести все группы юзеров, у которых одинаковый b. 
Требуемый аутпут:
70: user_1, user_2
19: user_3, user_4
1: user_5 

использовать defaultdict
"""

from collections import defaultdict


def get_b_report(data):
    groups = defaultdict(list)
    result = ""
    for user, values in data.items():
        groups[values['b']].append(user)
    for b, users in groups.items():
        join_users = ', '.join(users)
        result += "{b}: {join_users}\n".format(b=b, join_users=join_users)
    return result


def test_empty_report():
    test_data = {}
    expected_result = ""
    actual_result = get_b_report(test_data)
    if actual_result == expected_result:
        print("test_empty_report: ok")
    else:
        print("test_empty_report: fail")
        print(
            "Expected:\n{}\nactual:\n{}".format(expected_result, actual_result)
        )


def test_non_unique_b():
    test_data = dict(
        user_1=dict(a=10, b=70), 
        user_2=dict(a=12, b=70), 
        user_3=dict(a=7, b=19), 
        user_4=dict(a=12, b=19), 
        user_5=dict(a=55, b=1)
    )
    expected_result = "70: user_1, user_2\n19: user_3, user_4\n1: user_5\n"
    actual_result = get_b_report(test_data)
    if actual_result == expected_result:
        print("test_non_unique_b: ok")
    else:
        print("test_non_unique_b: fail")
        print(
            "Expected:\n{}\nactual:\n{}".format(expected_result, actual_result)
        )


def test_same_b_for_all_users():
    test_data = dict(
        user_1=dict(a=10, b=1),
        user_2=dict(a=12, b=1),
        user_3=dict(a=7, b=1),
        user_4=dict(a=12, b=1),
        user_5=dict(a=55, b=1)
    )
    expected_result = "1: user_1, user_2, user_3, user_4, user_5\n"
    actual_result = get_b_report(test_data)
    if actual_result == expected_result:
        print("test_same_b_for_all_users: ok")
    else:
        print("test_same_b_for_all_users: fail")
        print(
            "Expected:\n{},\nactual:\n{}".format(expected_result, actual_result)
        )


def test_report_all_b_different():
    test_data = dict(
        user_1=dict(a=10, b=70),
        user_2=dict(a=12, b=60),
        user_3=dict(a=7, b=50),
        user_4=dict(a=12, b=40),
        user_5=dict(a=55, b=30)
    )
    expected_result = \
        "70: user_1\n60: user_2\n50: user_3\n40: user_4\n30: user_5\n"
    actual_result = get_b_report(test_data)
    if actual_result == expected_result:
        print("test_report_all_b_different: ok")
    else:
        print("test_report_all_b_different: fail")
        print(
            "Expected:\n{},\nactual:\n{}".format(expected_result, actual_result)
        )


def test_extra_fields_in_data():
    test_data = dict(
        user_1=dict(a=10, b=70, c=10, d=70),
        user_2=dict(a=12, b=60, c=32, d=22),
        user_3=dict(a=7, b=50, c=5, d=22)
    )
    expected_result = "70: user_1\n60: user_2\n50: user_3\n"
    actual_result = get_b_report(test_data)
    if actual_result == expected_result:
        print("test_extra_fields_in_data: ok")
    else:
        print("test_extra_fields_in_data: fail")
        print(
            "Expected:\n{},\nactual:\n{}".format(expected_result, actual_result)
        )


if __name__ == "__main__":
    test_empty_report()
    test_non_unique_b()
    test_same_b_for_all_users()
    test_report_all_b_different()
    test_extra_fields_in_data()

