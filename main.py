rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# 1st Part - Asking user to make his Choice.

select = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))

if select >= 3 or select < 0:
  print("You typed wrong number. Select the right number")
else:
  lst = [rock, paper, scissors]
  user_select = (lst[(select)])
  print(user_select)

  #---------------------------------------------------------
  # 2nd Part - Using random module to let computer choose.

  print("Computer chose:")
  computer_select = random.choice(lst)
  print(computer_select)

  #---------------------------------------------------------
  # 3rd Part - Conditional statement for lettig user know who wins



  if (user_select == rock and computer_select == scissors ) or (user_select == scissors and computer_select == paper ) or (user_select == paper and computer_select == rock ):
    print("You WON!!! 😎")
  elif user_select == computer_select:
    print("DRAW!!!")
  else:
    print("You loose 😔")