import numpy as np

# Creating 2 arrays with family members height and weight

np_height = np.array([1.21, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 49.2, 103.6, 55.4, 188.7])
# Calculating the BMI

fam_BMI = np_weight / (np_height ** 2)

# The For Loop categorises the BMI for every family member

print("-" * 60)
for bmi in fam_BMI:
    print(f'The BMI for the family member is {bmi}')

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

    print("-" * 60)