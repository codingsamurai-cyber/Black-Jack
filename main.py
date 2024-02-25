import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card():
    return random.choice(cards)


user_cards = [random_card(), random_card()]
computer_cards = [random_card(), random_card()]


def calculate_score(deck):
    score = sum(deck)
    if 11 in deck and 10 in deck and score == 21:
        return 0
    if score > 21:
        if 11 in deck:
            deck.remove(11)
            deck.append(1)
    return score


computer_score = calculate_score(computer_cards)
user_score = calculate_score(user_cards)

game_state = False

while not game_state:
    print(f"Your cards are {user_cards}, current score is {user_score}")
    print(f"Dealer's first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_state = True
    else:
        decision = input("Would you get another card? y/n \n")
        if decision == "y":
            user_cards.append(random_card())
            user_score = calculate_score(user_cards)
        elif decision == "n":
            game_state = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(random_card())
    computer_score = calculate_score(computer_cards)


def compare():
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lose"
    elif user_score == 0:
        return "you win"
    elif user_score > 21:
        return "you lose"
    elif computer_score > 21:
        return "you win"
    elif user_score > computer_score:
        return "you win"
    elif computer_score > user_score:
        return "you lose"


print(compare())
print(computer_cards)
