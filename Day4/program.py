                         # Rock Paper Scissors Game #
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

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))

computerChoice = random.randint(0, 2)
print(f"Computer chose {computerChoice}")

if playerChoice == 0 and computerChoice == 2:
    print("You win!")
elif computerChoice > playerChoice:
    print("You lose!")
else: 
    print("You typed an invalid number.")