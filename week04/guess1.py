# Prompt User to Guess Number
# Author: Michal Gondek

numberToGuess = 15

guess = int(input('Please guess the Number:'))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ('too low')

    else: print ('too high')

    guess = int(input('Please guess again:'))

print ('Well Done! Yes the number was', numberToGuess) 
