import random
a = random.randint(0,200)
print(a)
guess = int(input('Guess a number from 1-200: '))
counterPlayer = 0
while True:
    if guess == a:
        print('You guessed the number')
        break
    elif guess > a:
        print('You guessed too high. Try again.')
        guess = int(input('Guess again: '))
        counterPlayer += 1
    elif guess < a:
        print('You guess too low. Try again.')
        guess = int(input('Guess again: '))
        counterPlayer += 1
print('It took you: ' + str(counterPlayer) + ' guessed the number')
            


#*****TO DO****#
#add computer guess AI#
#add guess  AI#
#compare guess counter to see who won#

