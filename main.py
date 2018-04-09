import slots
import war 
import wallet
import sys
import time
import random

def welcome():
  time.sleep(1)
  print('Welcome to the Bottega Casino!')
  print(game_choice())
def game_choice():
  print('You start with $10! Use it wisely, when it\'s gone, that means Game Over...and you die....')
  time.sleep(5)
  print('Just Kidding')
  time.sleep(3)
  print('....probably.')
  print('Anyways, Please choose a game you would like to play:')
  print('war or slots')
  answer = input('')
  time.sleep(1)
  if (answer == 'war'):
    print(war())
  elif answer == 'slots':
    print(slots())
  elif answer == 'close':
    sys.exit("Program Closing...")
  else: 
    print ('Invalid Input. Please try again.')
    time.sleep(1)
    print(game_choice())
print(welcome())