def slots():  
  wheels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  
  def slot():
    first_wheel = random.choice(list(wheels))
    second_wheel = random.choice(list(wheels))
    third_wheel = random.choice(list(wheels))
    print(first_wheel)
    time.sleep(1)
    print(second_wheel)
    time.sleep(1)
    print(third_wheel)
    payout = first_wheel
    time.sleep(1)
    if first_wheel == 7 and second_wheel == 7 and third_wheel == 7:
      payout = 100
      print(f'JACKPOT! Your win ${payout}! WOW!')
    elif first_wheel == second_wheel == third_wheel:
      payout = first_wheel*2
      print(f'You win ${payout}! :)')
    elif first_wheel == second_wheel or second_wheel == third_wheel:
      payout = second_wheel
      print(f'You win ${payout}! :)')
    elif first_wheel == third_wheel:
      payout = first_wheel
      print(f'You win ${payout}! :)')
    else:
      print('No winnings. :(')
      time.sleep(1)
    print(play_again_slots())
      
  def invalid_input_slots():
    print('Are you ready?')
    answer = input('')
    if answer == 'yes':
      print('Let\'s play!')
      print(slot())
    elif answer == 'no':
      print('Ok, come back later.')
      print("Returning to menu...")
      time.sleep(1)
      print(welcome())
    else: 
      print ('Invalid Input. Please try again.')
      print(invalid_input_slots())
      
  def play_again_slots():
    print('Play Again?')
    answer = input('')
    time.sleep(1)
    if answer == 'yes':
      print(slot())
    elif answer == 'no':
      print('That\'s ok. This was fun! Please come again.')
      time.sleep(2)
      print('Returning to menu...')
      time.sleep(1)
      print(welcome())
    else:
      print('Invalid Input. Please try again.')
      print(play_again_slots())
  
  def welcome_slots():
    time.sleep(2)
    print('Welcome to Bottega Slots!')
    time.sleep(1)
    print('Here\'s how it works: Spin the numbers, win some money! Each spin will cost you $1. Any match of two numbers will win, a triple will get you double, but the Jackpot is all sevens!')
    time.sleep(5)
    print('Are you ready?')
    answer = input('')
    time.sleep(1)
    if (answer == 'yes'):
      print('Let\'s play!')
      print(slot())
    elif answer == 'no':
      print('Ok, come back later.')
      print("Returning to menu...")
      print(welcome())
    else: 
      print ('Invalid Input. Please try again.')
      print(invalid_input_slots())
  print(welcome_slots())