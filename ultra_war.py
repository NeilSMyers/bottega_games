import random

deck = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}

def hand():
  player_hand = 26
  my_hand = 26
  while player_hand and my_hand > 0:
    player_card = random.choice(list(deck))
    player_card_value = deck[player_card]
    my_card = (random.choice(list(deck)))
    my_card_value = deck[my_card]
    if (player_card_value < my_card_value):
      player_hand -= 1
      my_hand += 1
    elif (player_card_value == my_card_value):
      while player_card == my_card:
        player_card = random.choice(list(deck))
        player_card_value = deck[player_card]
        my_card = (random.choice(list(deck)))
        my_card_value = deck[my_card]
        if (player_card_value < my_card_value):
          player_hand -= 5
          my_hand += 5
        elif (player_card_value == my_card_value):
          continue
        else:
          player_hand += 5
          my_hand -= 5
    else:
      player_hand += 1
      my_hand -= 1
    if player_hand <= 0:
      print("Computer Wins.")
      break
    elif my_hand <= 0:
      print("You Win.")
      break
hand()