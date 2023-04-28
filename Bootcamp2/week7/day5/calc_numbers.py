def add_numbers(num1, num2):
    """adds numbers"""
    sum = num1 + num2

    return sum

def multiply_numbers(num1, num2):
    """multiplies numbers"""
    mult = num1 * num2

    return mult

def subtract_numbers(num1, num2):
    """subtracts numbers"""
    sub = num1 - num2

    return sub


def divide_numbers(num1, num2):
    """divides numbers"""
    divide = num1 / num2

    return divide


num1 = int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

print(num1, num2)
total1 = add_numbers(num1, num2)
print("the sum is:", total1)
total2 = multiply_numbers(num1, num2)
print("The product is:", total2)
total3 = subtract_numbers(num1, num2)
print("the difference is:", total3)
total4 = divide_numbers(num1, num2)
print("the division is:", total4)