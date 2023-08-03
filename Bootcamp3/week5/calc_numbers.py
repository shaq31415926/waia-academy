def add_numbers(number1, number2):
    """This functions add two numbers"""
    add = number1 + number2
    return add


def multiply_numbers(number1, number2):
    """This functions multiplies two numbers"""
    product = number1 * number2
    return product


def subtract_numbers(number1, number2):
    """This functions subtracts two numbers"""
    difference = number1 - number2
    return difference


def divide_numbers(number1, number2):
    """This functions divides two numbers"""
    division = number1 / number2
    return division


num1 = 5
num2 = 10
num3 = 63764

total1 = add_numbers(num1, num2)
print(total1)
total2 = multiply_numbers(total1, num1)
print(total2)
total3 = divide_numbers(total2, total1)
print(total3)
total4 = subtract_numbers(total3, total1)
print(total4)
