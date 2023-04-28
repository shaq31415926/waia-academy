num1 = int(input("Please enter number1:"))
operator = input("Please enter the operator [+, -, *, /]:")
num2 = int(input("Please enter number2:"))


def calculations(num1, num2):
    if operator == "+":
        total = num1 + num2
    elif operator == "-":
        total = num1 - num2
    elif operator == "*":
        total = num1 * num2
    elif operator == "/":
        total = num1 / num2
    else:
        total = "ERORR"

    return total

total = calculations(num1, num2)
if total == "ERROR":
    print("Operator not recognised")
else:
    print(f"The total is {total}")

