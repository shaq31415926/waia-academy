height = int(input("Please enter your height:"))
weight = int(input("Please enter weight:"))


def bmi_calculations(height, weight):
    bmi = weight / height ** 2

    if bmi < 18.5:
        print("They are considered Underweight")

    elif bmi <= 24.9 and bmi >= 18.5:
        print("They are considered Healthy")

    elif bmi >= 25 and bmi <= 29.9:
        print("They are considered Overweight")

    elif bmi > 30:
        print('They are considered Obese')

    else:
        print('incorrect input')

bmi_calculations(height, weight)