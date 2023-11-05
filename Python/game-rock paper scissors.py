import random
import graphics

choices = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
if user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)
    print(f"You choose {user_choice}.")
    if user_choice == "rock":
        print(graphics.rock)
    elif user_choice == "paper":
        print(graphics.paper)
    else:
        print(graphics.scissors)

    print(f"The computer choose {computer_choice}.")
    if computer_choice == "rock":
        print(graphics.rock)
    elif computer_choice == "paper":
        print(graphics.paper)
    else:
        print(graphics.scissors)


    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
