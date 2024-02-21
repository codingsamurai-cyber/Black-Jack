import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack():
    user_cards = [11, 11]
    computer_cards = [random.choice(cards), random.choice(cards)]
    sum_user = sum(user_cards)
    sum_comp = sum(computer_cards)
    print(user_cards)
    print(computer_cards)
    print(sum_user)
    print(sum_comp)
    print(computer_cards[0])

    if sum_comp == 21:
        print("Computer wins")
    elif sum_comp > 21:
        print("Computer loses")
    if sum_user == 21:
        print("You win")
    elif sum_user > 21:
        print("You lose")
        if 11 in user_cards:
            user_cards[user_cards.index(11)] = 1
            if sum(user_cards) > 21:
                add_card = input("Do you want to get another card? y/n")
                if add_card == "y":
                    decision = True
                    user_cards.append(random.choice(cards))
                    print(user_cards)
                if add_card == "n":
                    decision = False
            else:
                print("You lose")
    if sum_user == 21 and sum_comp == 21:
        print("It's a draw")


black_jack()