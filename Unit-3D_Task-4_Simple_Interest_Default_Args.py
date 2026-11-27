# Example: function defined using two parameters
def divide(a, b):  # a, b are 2 parameters
    return a / b


result = divide(a=10, b=20)  # with keyword arguments
print(result)  # Output: 0.5 (note: 10 / 20 is 0.5)

result = divide(10, 20)  # positional arguments
print(result)  # Output: 0.5