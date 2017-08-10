import turtle 
print('Welcome to Hangman')
#drawing Hangman
def Hangman(tu):
    tu.ht()
    tu.forward(80)
    tu.right(90)
    tu.forward(50)
    tu.penup()
    tu.goto(55,-76)
    tu.pendown()
    tu.circle(25)
    tu.penup()
    tu.goto(80,-100)
    tu.pendown()
    tu.forward(40)
    tu.left(90)
    tu.forward(50)
    tu.backward(100)
    tu.forward(50)
    tu.right(90)
    tu.forward(90)
    tu.left(45)
    tu.forward(80)
    tu.backward(80)
    tu.right(90)
    tu.forward(80)
#calling the function to make drawing work
Hangman(turtle)

user1 = input('Enter a word:')
user1.lower()

def guessing(user):
    li = list(user)
    guess = input('Guess a letter: ')
    totalGuesses = 6
    while True: 
        if guess ==li:
            li.remove(guess)
            print("You've gussed one right.")
            guess = input('Guess another letter')
        elif len(li) == 0:
            print("You've guessed all of the words.")
            break
        elif guess != li:
            print("You didn't guess correctly, try again")
            guess = input('Guess another letter')
        if totalGuesses == li:
                print('You lose.')
                break
            
            

    
        
        
    

guessing(user1)


