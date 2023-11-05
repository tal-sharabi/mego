import random
import graphics


def welcome_message():
    print('Welcome to "Hangman"!\n')
    print(graphics.logo)


def choose_random_word():
    word_list = ["simon", "meir", "haim", "noam", "reut"]
    return random.choice(word_list)


def display_word(word_to_guess, correctly_guessed):
    display = ""
    for letter in word_to_guess:
        if letter in correctly_guessed:
            display += letter
        else:
            display += "_ "
    return display


def main_game_loop():
    word_to_guess = choose_random_word()
    word_display = "_ " * len(word_to_guess)
    wrong_guesses = 0
    correctly_guessed = ""

    while wrong_guesses < 6 and word_display != word_to_guess:
        word_display = display_word(word_to_guess, correctly_guessed)
        print(word_display)

        if word_display == word_to_guess:
            print("Congratulations! You've guessed the word:", word_to_guess)
            print(graphics.trophy)
            break

        user_letter = input("Enter a letter: ").lower()

        if user_letter in word_to_guess:
            correctly_guessed += user_letter
        else:
            wrong_guesses += 1
            print(graphics.hangman_pics[wrong_guesses - 1])
            print("Incorrect guess!")

    if word_display != word_to_guess:
        print(graphics.hangman_pics[6])
        print(graphics.game_over)
        print(f"\nThe right answer is {word_to_guess}")


def play_hangman_game():
    welcome_message()
    main_game_loop()


if __name__ == "__main__":
    play_hangman_game()
