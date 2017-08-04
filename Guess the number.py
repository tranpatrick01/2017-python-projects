import random
a = random.randint(0,200)
print(a)
guess = int(input('Guess a number from 1-200: '))
while True:
    if guess == a:
        print('You guessed the number')
        break
    elif guess > a:
        print('You guessed too high. Try again.')
        guess = int(input('Guess again'))
    elif guess < a:
        print('You guess too low. Try again.')
        guess = int(input('Guess again'))
    
            


#*****TO DO****#
#add computer guess AI#
#add guess counter for user and AI#
#compare guess counter to see who won#

