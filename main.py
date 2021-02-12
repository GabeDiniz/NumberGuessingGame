import random

# Introduction
n_range = int(input('Pick your range! Guess from 1 to? (input a number > 1) ')) 
guesses = int(input('Pick how many guesses you would like! (input a number > 1) '))
number = random.randint(1, n_range)

def number_guesser(n_range, guesses, number, initial_n):
  
  guess = int(input('What is your guess? '))

  if number > guess:
    print('Wrong. The number is greater!')

  elif number < guess:
    print('Wrong. The number is smaller!')

  elif number == guess:
    if guesses == initial_n:
      print('FIRST TRY??? Great job!')
    else:
      print('Great job! You guessed the number!')
    return

  guesses -= 1
  
  if guesses == 1:
    print('Last guess!!!')

  if guesses == 0:
    print("Sorry you're out of guesses. The number was", number)
  else:
    return number_guesser(n_range, guesses, number, initial_n)
  



number_guesser(n_range, guesses, number, guesses)
