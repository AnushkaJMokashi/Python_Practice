# Python callable types are a way of specifying that an object can be called like a function, with parentheses and arguments. For example, `lambda x: x**2` is a callable type that represents a function that takes one argument `x` and returns its square. You can use the `typing.Callable` type from the `typing` module to indicate that an object is callable. For example, `typing.Callable[[int, str], bool]` means that the object is callable with two arguments of type `int` and `str`, and returns a value of type `bool`.

# There are many examples of callable types in Python, such as built-in functions, user-defined functions, methods of classes, and instances of classes that define the `__call__` method. The `__call__` method is a special method that allows an object to be invoked as if it were a function. For example, you can define a class that represents a calculator with the following code:

def greeting(name: str) -> str:
    return 'Hello ' + name
# In the function greeting, the argument name is expected to be of type str and
# the return type str. Subtypes are accepted as arguments.

# The typing module is used for type hints:

# This module provides runtime support for type hints.

# What are type hints?
# The documentation provides this example:

def greeting(name: str) -> str:
    return 'Hello ' + name
# In the function greeting, the argument name is expected to be of type str and the return type str. Subtypes are accepted as arguments.

# How to use typing.Callable
# Assume you want to define a function that takes two integers and performs some kind of operation on them that returns another integer:

def apply_func(a: int, b: int, func) -> int:
    return func(a, b)

# So the expected type of the func argument in apply_func is "something that can be called (e.g. a function) that takes two integer arguments and returns an integer":

# typing.Callable[[int, int], int]