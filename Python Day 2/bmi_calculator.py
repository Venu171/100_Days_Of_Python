"""
The body mass index (BMI) is a measure 
used in medicine to see if someone is underweight or overweight.
This is the formula used to calculate it:
bmi is equal to the person's weight divided by the person's height squared.
"""


def bmi_calculator():
    weight = float(input("Enter the weight in kg:"))
    height = float(input("Enter the height in mts:"))
    bmi = (weight/(height**2))
    print(f"Your BMI is {round(bmi)}")


if __name__ == "__main__":
    bmi_calculator()
