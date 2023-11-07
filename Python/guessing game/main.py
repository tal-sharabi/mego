import random
import graphics

# Constants
HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


# Function to choose the difficulty level
def choose_difficulty():
    while True:
        difficulty = input("Choose the difficulty (easy/hard): ").lower()
        if difficulty == 'easy':
            return EASY_ATTEMPTS
        elif difficulty == 'hard':
            return HARD_ATTEMPTS
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")


# Function to play the guessing game
def play_guessing_game():
    attempts = choose_difficulty()
    number_to_guess = random.randint(1, 100)

    while attempts > 0:
        guess = int(input(f"You have {attempts} tries. Guess the number (1-100): "))

        if guess < number_to_guess:
            print("Too low. Guess again.")
        elif guess > number_to_guess:
            print("Too high. Guess again.")
        else:
            print("Yes!")
            print(graphics.trophy)
            break

        attempts -= 1
        if attempts > 0:
            continue
        else:
            print(graphics.game_over)
            print(f"The number was {number_to_guess}.")



print("Welcome to the guessing game!")
print(graphics.logo)
play_guessing_game()



