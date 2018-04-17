import random
import sys

words =['cat','dog','loser','word','table','pocket', 'juice','sausage','pumpkin']
word = random.choice(list(words))
letters = len(word)

def guess():
  guesses = 1
  while guesses < 11:
    guess = input('')
    if guess == word:
      print('Wow. You got it. You\'re not awful. bye.')
      sys.exit("System Shutting Down: waiting for less skilled player.")
    elif guess in word:
      print(f'{guess} IS in the word.')
    else:
      print('Wrong, you suck.')
      print('Guess Again!')
      guesses += 1
  print("You have exceeded your guesses. Guess the word or die.")
  final_chance = input('')
  if final_chance == word:
    print("Ugh! Fine! you win.")
    sys.exit("I'm angry.")
  else: 
    print(f'HAHA! You Lose! The word was "{word}."')
    sys.exit("Go cry.")

def hang_man():
  print(f'The word is {letters} letters long.')
  print('What is your first guess?')
  print(guess())

def welcome():
  print('Welcome to hang man!')
  print('A word will be selected at random, you have 10 strikes to get the word. You can guess the word at any time, when you have used all your guesses, you will have one final chance to guess the word...or die haha. ya...so ya.')
  print("Here we go! Ready?")
  ready = input('')
  if ready == 'yes':
    print(hang_man())
  else:
    sys.exit("Fine, don't play....jerk")

welcome()