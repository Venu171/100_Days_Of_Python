"""
The body mass index (BMI) is a measure 
used in medicine to see if someone is underweight or overweight.
This is the formula used to calculate it:
bmi is equal to the person's weight divided by the person's height squared.

If the bmi is under 18.5 (not including), print out "underweight"
If the bmi is between 18.5 (including) and 25 (not including),
print out "normal weight"
If the bmi is 25 (including) or over, print out "overweight"
"""


def bmi_calculator_with_interpretations():
    weight = float(input("Enter your weight in kgs: "))
    height = float(input("Enter your height in mts: "))
    bmi = weight/(height**2)
    if bmi < 18.5:
        print("You're underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("You're normal weight")
    elif bmi >= 25:
        print("You're overweight")


if __name__ == "__main__":
    bmi_calculator_with_interpretations()
