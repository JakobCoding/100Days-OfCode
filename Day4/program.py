import random                      # Rock Paper Scissors #
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
gameImages = [rock, paper, scissors]
playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))
if playerChoice >=0 and playerChoice <= 2:
    print(gameImages[playerChoice])

computerChoice = random.randint(0, 2)
print(f"Computer chose {computerChoice}")

if playerChoice >=3 or playerChoice < 0:
    print("You typed an invalid number, You lose!")
elif playerChoice == 0 and computerChoice == 2:
    print("You win!")
elif computerChoice == 0 and playerChoice ==2:
    print("You lose!")
elif computerChoice > playerChoice:
    print("You lose!")
elif playerChoice > computerChoice:
    print("You win!")
elif playerChoice == computerChoice:
    print("It's a draw!")
