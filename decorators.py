
# Allows you to modify behavior of the function without changing the function

import base64

def decorator_function(func):
    def wrapper(arg):
        func(arg)
        print("""\nThe string above needs to be passed as a bytes object to be base64 encoded. This string, including the following output is part of the decorator\n \n""")
        turn_to_bytes = bytes(arg, 'utf-8')
        string = base64.b64encode(turn_to_bytes)
        print(f"The decorator function served to turn the string into: \n \n \t {string}")
    return wrapper


def second_decorator(func):
    def wrapper(arg):
        func(arg)
        print("""\nWe will now decode the base64 string\n \n""")
        turn_to_bytes =  bytes(arg, 'utf-8')
        string = base64.b64decode(arg)
        print(f"The content of the base64 encoded string that the decorator converted: \n \n \t {string}")
    return wrapper


@decorator_function
def decorated_function(arg):
    return decorated_function
    

@decorator_function
def dec2_function(arg):
    return arg


@second_decorator
def b64_string_input(arg):
    return arg

    
decorated_function(input("\nThis is the original string that was passed in: \n \t"))

dec2_function(input("\n \nOur second passed in string: \n \t"))

b64_string_input(input("\n \nOur base64 encoded string input: \n \t" ))
