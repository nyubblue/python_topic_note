import random
from unittest import result

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_scores, comp_scores):
    if u_scores == comp_scores or (u_scores > 21 and comp_scores > 21):
        return "Draw"
    elif comp_scores > 21 or u_scores > comp_scores:
        return "You Win!"
    else :
       return "You lose!"

def play_game():
    user_cards = []
    computer_card = []
    is_end_game = False
    result_game = ""

    for _ in range(2):
        user_cards.append(deal_card())
        computer_card.append(deal_card())

    user_scores = calculate_score(user_cards)
    computer_scores = calculate_score(computer_card)
    print(f"   Your cards: {user_cards}, current score: {user_scores}")
    print(f"   Computer's first card: {computer_card[0]}")

    """check : "is BlackJack ?" """
    if user_scores == 21 and computer_scores == 21:
        is_end_game = True
        result_game = "Draw"
    elif user_scores == 21:
        is_end_game = True
        result_game = "You Win!"
    elif computer_scores == 21:
        is_end_game = True
        result_game = "You lose!"
    else:
        """ Do you want to continue ? """
        while not is_end_game:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_scores = calculate_score(user_cards)
                print(f"   Your cards: {user_cards}, current score: {user_scores}")
                print(f"   Computer's first card: {computer_card[0]}")
                if user_scores > 21:
                    is_end_game = True
            else:
                is_end_game = True

    while computer_scores != 0 and computer_scores < 17:
        computer_card.append(deal_card())
        computer_scores = calculate_score(computer_card)

    result_game = compare(user_scores, computer_scores)
    print("\n" + result_game)
    print(f"   Your final hand: {user_cards}, final score: {user_scores}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_scores}")
    print(compare(user_scores, computer_scores))

play_game()
    