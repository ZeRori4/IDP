class Func:

    def func(self, user_function, arg_1, arg_2):
        if user_function == "+":
            return arg_1 + arg_2
        elif user_function == "-":
            return arg_1 - arg_2
        elif user_function == "*":
            return arg_1 * arg_2
        elif user_function == "/":
            return arg_1 / arg_2


function = Func()