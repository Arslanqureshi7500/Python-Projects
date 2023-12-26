import random
from clear import clear
from art import logo


def deal_card():
    """"This function return choose a randomly card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """"This function is to calculate the score of list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):

    """"This function return conditionally statement"""

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    if computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    if user_score == 0:
        return "Win with a Blackjack 😎"
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Opponent went over. You win 😁"
    if user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """"This function is used for restart the game"""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_ended = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_ended:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Card's {user_cards} and score is {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 and user_score > 21:
            is_game_ended = True
        else:
            should_continue = input("If you want to draw another card, type 'Yes' or 'No': ").lower()
            if should_continue == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_ended = True

    while computer_score!=0 and computer_score<17:
        computer_card = computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()


