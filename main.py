import random
from replit import clear
from art import logo

def initial_setup(): 
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  #validation
  if play != 'y' and play != 'n':
    print("Please type 'y' or 'n'")
    return initial_setup()

  if play == 'n':
    print("Okay, maybe another time :(")
    return
  return play == 'y'

def calculate_sum(cards):
  card_sum = sum(cards)

  #changes ace value from 11 to 1 if user would otherwise go over
  if card_sum > 21 and 11 in cards:
    ace_ind = cards.index(11)
    cards[ace_ind] = 1
    card_sum = sum(cards)
    
  return card_sum

def deal_cards(num):
  """Returns an array with the random amount of cards requested"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cards_drawn = random.sample(cards, num)
  return cards_drawn

def ask_another_card():
  another_card = input("Type 'y' to get another card, type 'n' to pass: ")

  if another_card != 'y' and another_card != 'n':
    return ask_another_card()
  return another_card == 'y'

def print_card_data(user, computer):
  print(f"Your cards: {user['cards']}, current score: {user['score']}")
  print(f"Computer's first card: {computer['cards'][0]}")
  return ask_another_card()

def get_result_text(user_score, comp_score):
  result_text = ""
  if user_score > comp_score and user_score < 22 and comp_score != 21:
    result_text = "You win! 😁"
  elif comp_score == user_score and user_score == 21:
    result_text = "It's a tie.🧐"
  elif comp_score == user_score and user_score:
    result_text = "It's a push.😮‍💨"
  else:
    result_text = "You lose lol.😭"
  return result_text

def show_results(user, comp):
  print(f"Your final hand: {user['cards']}, final score: {user['score']}")
  print(f"Computer's final hand: {comp['cards']}, final score: {comp['score']}")
  result_text = get_result_text(user['score'], comp['score'])
  print(f"{result_text}")
  clear()

def run():
  game_active = False
  continue_dealing = False
  
  while not game_active:
    wants_to_play = initial_setup()

    if wants_to_play:
      print(logo)
      game_active = True
      user_data = {}
      computer_data = {}
  
  while game_active:
    user_data["cards"] = deal_cards(2)
    user_data["score"] = calculate_sum(user_data["cards"])
    computer_data["cards"] = deal_cards(1)

    while  calculate_sum(computer_data["cards"]) < 17:
      additional_deal = deal_cards(1)[0]
      if calculate_sum(computer_data["cards"]) + additional_deal < 22:
        computer_data["cards"].append(additional_deal)
    computer_data["score"] = calculate_sum(computer_data["cards"])     
    wants_another_card = print_card_data(user_data, computer_data)
    
    if wants_another_card:
      continue_dealing = True
    else:
      show_results(user_data, computer_data)
      game_active = False
      run()

    while continue_dealing:
      user_data["cards"] += deal_cards(1)
      user_data["score"] = calculate_sum(user_data["cards"])

      #trigger end of game if user gets blackjack or busts
      if user_data["score"] >= 21:
        show_results(user_data, computer_data)
        continue_dealing = False
        game_active = False
        run()
        
      wants_another_card = print_card_data(user_data, computer_data)

      if not wants_another_card:
        show_results(user_data, computer_data)
        continue_dealing = False
        game_active = False
        run()
run()

