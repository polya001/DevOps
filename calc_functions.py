"""
Module with basic calc functions
"""

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
   
        if y == 0:
            return "ERROR"
        return x / y
