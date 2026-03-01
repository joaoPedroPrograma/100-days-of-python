import random

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
game = ["Rock", "Paper", "Scissors"]
ascii_art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
]
computer = random.randint(0, 2)
print(ascii_art[userChoice])
print("The computer chose", game[computer])
print(ascii_art[computer])
if userChoice == computer:
    print("It's a draw!")
elif userChoice == 0 and computer == 2:
    print("You smashed the scissor!")
elif userChoice == 1 and computer == 0:
    print("You covered the rock!")
elif userChoice == 2 and computer == 1:
    print("Death by a thousand cuts! You won!")
else:
    print("You lost")