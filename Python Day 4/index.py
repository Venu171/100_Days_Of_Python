import random
# Rock Paper Scissors ASCII Art

# Rock
var_0 = """
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
var_1 = """
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
var_2 = """
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# 0>2,1>0,2>1
your_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computer_choice = random.randrange(0, 3)
choose_var_your = None
choose_var_computer = None
if your_choice == 0:
    choose_var_your = var_0
elif your_choice == 1:
    choose_var_your = var_1
elif your_choice == 2:
    choose_var_your = var_2

if computer_choice == 0:
    choose_var_computer = var_0
elif computer_choice == 1:
    choose_var_computer = var_1
elif computer_choice == 2:
    choose_var_computer = var_2

print(f"You choose \n{choose_var_your}")
print(f"Computer choose \n{choose_var_computer}")
if your_choice == 0:
    if computer_choice == 1:
        print('Computer Wins!')
    elif computer_choice == 2:
        print('You Wins!')
    else:
        print('It\'s a draw or Something went wrong')
elif your_choice == 1:
    if computer_choice == 0:
        print('You Wins!')
    elif computer_choice == 2:
        print('Computer Wins!')
    else:
        print('It\'s a draw or Something went wrong')
elif your_choice == 2:
    if computer_choice == 0:
        print('Computer Wins!')
    elif computer_choice == 1:
        print('You Wins!')
    else:
        print('It\'s a draw or Something went wrong')
else:
    print('Something went wrong')
