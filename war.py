def war():
  deck = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}
  
  def hand():
    print('Your card is:')
    player_card = random.choice(list(deck))
    time.sleep(1)
    print(player_card)
    player_card_value = deck[player_card]
    time.sleep(1)
    print('My card is:')
    time.sleep(1)
    my_card = (random.choice(list(deck)))
    print(my_card)
    my_card_value = deck[my_card]
    time.sleep(1)
    if (player_card_value < my_card_value):
      print('You Lose :(')
      print(play_again_war())
    elif (player_card_value == my_card_value):
      print('WAR!')
      time.sleep(1)
      print(hand())
    else:
      print('You Win! :)')
      time.sleep(1)
      print(play_again_war())
      
  def invalid_input_war():
    print('Are you ready?')
    answer = input('')
    time.sleep(1)
    if answer == 'yes':
      print('Let\'s play!')
      print(hand())
    elif answer == 'no':
      print('Ok, come back later.')
      print("Returning to menu...")
      time.sleep(2)
      print(welcome())
    else: 
      print ('Invalid Input. Please try again.')
      print(invalid_input_war())
      
  def play_again_war():
    print('Play Again?')
    answer = input('')
    time.sleep(1)
    if answer == 'yes':
      print(hand())
    elif answer == 'no':
      print('That\'s ok. This was fun! Please come again.')
      time.sleep(1)
      print('Returning to menu...')
      print(welcome())
    else:
      print('Invalid Input. Please try again.')
      print(play_again_war())
      
  def welcome_war():
    time.sleep(1)
    print('Welcome to war!')
    time.sleep(1)
    print('Here\'s how it works: You will recieve a card, you\'ll then have a chance to place a bet, then I will recieve a card, whoever has the highest card wins. Simple enough, right?')
    time.sleep(5)
    print('Are you ready?')
    answer = input('')
    time.sleep(1)
    if (answer == 'yes'):
      print('Let\'s play!')
      time.sleep(1)
      print(hand())
    elif answer == 'no':
      print('Ok, come back later.')
      time.sleep(1)
      print('Returning to menu...')
      time.sleep(2)
      print(welcome())
    else: 
      print ('Invalid Input. Please try again.')
      print(invalid_input_war())
  print(welcome_war())