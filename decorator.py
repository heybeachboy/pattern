"""
new decorator continer
"""
from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapperTheFunction():
        print("I am doing boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapperTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell ")

decorator = a_new_decorator(a_function_requiring_decoration) 
decorator()
print(decorator.__name__)
