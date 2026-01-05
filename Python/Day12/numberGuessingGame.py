import random

EASY_MODE = 10
HARD_MODE = 5

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100 (both including).")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if mode == 'easy':
    attempts = EASY_MODE
else:
    attempts = HARD_MODE

num_to_guess = random.randint(1, 100)
guess_status = False

while attempts > 0 and guess_status == False:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess != num_to_guess:
        attempts -= 1
        if guess > num_to_guess:
            print("Too high.\nGuess again.")
        elif guess < num_to_guess:
            print("Too low.\nGuess again.")
    else:
        print(f"You got it! The answer was {num_to_guess}.")
        guess_status = True

if attempts == 0:
    print("You've run out of guesses, you lose.")