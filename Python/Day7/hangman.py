# pip install wonderwords
from wonderwords import RandomWord

# ASCII art for hangman

def printUserGuess(l):
    print("Word to guess:", end = " ")
    for x in l:
        print(x, end = " ")   
    print()

final_word = RandomWord().word()

user_guess = []
gameOver = -1
hangmanLives = 6

for ch in range(len(final_word)):
    user_guess.append('_')

guess_remaining = final_word

while gameOver == -1:

    printUserGuess(user_guess)
    user_input = input("Guess a letter: ")

    ind = [i for i, val in enumerate(guess_remaining) if val == user_input]

    if len(ind) != 0:
        for i in ind:
            user_guess[i] = user_input
            guess_remaining[i] = " "
    else:
        hangmanLives -= 1
        print(f"You guessed {user_input}, that's not in the word. You lose a life.")
    
    print(f"***********************{hangmanLives}/6 LIVES LEFT*************************")

    if hangmanLives == 0:
        gameOver = 0
    
    blank = [i for i, val in enumerate(user_guess) if val == "_"]
    if len(blank) == 0:
        gameOver = 1

print(user_guess)
if gameOver == 1:
    print(f"You Win!")
else:
    print(f"It was {final_word}. You Lose!")