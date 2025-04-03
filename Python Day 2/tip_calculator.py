def tip_calculator():
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill? $"))
    percentage_tip = float(
        input("How much tip would you like to give? 10, 12, or 15? "))
    total_persons = float(input("How many people to split the bill? "))
    each_split = (total_bill+(percentage_tip*(total_bill/100)))/total_persons
    print(f"Each person should pay: ${each_split:.2f}")


if __name__ == "__main__":
    tip_calculator()
