# Rock Paper Scissors Game #
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