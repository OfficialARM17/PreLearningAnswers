import random

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def give_feedback(guess, secret_number):
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")


def play_game(secret_number):
    attempts = 0
    previous_guess = None 
    while True:
        guess = get_user_guess()

        if guess != previous_guess:
            attempts += 1
            previous_guess = guess

        if guess == secret_number:
            print(f"You Won! It took you {attempts} attempts.")
            break
        else:
            give_feedback(guess, secret_number)


def main():
    """
    Main function to initialize the game.
    """
    print("Welcome to the Guessing Game!")
    secret_number = random.randint(1, 100)
    play_game(secret_number)


main()
