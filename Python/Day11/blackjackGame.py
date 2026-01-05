import random
import os

deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def card_values(c):
    if c in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(c)
    elif c in ['J', 'Q', 'K']:
        return 10
    elif c in ['A']:
        return 11

def card_total(hand):
    sum = 0
    a = 0
    for h in hand:
        sum += card_values(h)
        if h == 'A':
            a += 1

    while sum > 21 and a > 0:
        sum -= 10
        a -= 1

    return sum

play_game = 'y'

while play_game == 'y':

    os.system('cls')
    deck_of_cards = deck
    hands = {
        0: [],  # user hand
        1: [],  # computer hand
    }

    # phase 1 - card distribution
    for i in range(1, 5):
        card = random.choice(deck_of_cards)
        deck_of_cards.remove(card)

        hands[i % 2].append(card)

    print(f"Your cards: {hands[0]}")
    print(f"Computer's first card: {hands[1][0]}")

    user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while user_choice == 'y' and card_total(hands[0]) <= 21:
        
        card = random.choice(deck_of_cards)
        deck_of_cards.remove(card)

        hands[0].append(card) # add a card to user's hand

        print(f"Your cards: {hands[0]}")
        print(f"Computer's first card: {hands[1][0]}")
        
        if card_total(hands[0]) > 21:
            print(f"Your final hand: {hands[0]} and the total exceeds 21.")
            print("Dealer Wins!!")
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if user_choice == 'n':

        while card_total(hands[1]) < 17:
            card = random.choice(deck_of_cards)
            deck_of_cards.remove(card)

            hands[1].append(card) # add a card to user's hand

        print(f"Your final hand: {hands[0]}")
        print(f"Computer's final hand: {hands[1]}")

         # calculate the sum of each hands to determine the winner
        user_sum = card_total(hands[0])
        cpu_sum = card_total(hands[1])

        if (user_sum <=21 and user_sum > cpu_sum) or cpu_sum > 21:
            print("You Win!")
        elif user_sum == cpu_sum:
            print("It's a draw.")
        else:
            print("Dealer Wins!!")

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()