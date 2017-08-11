import turtle 
print('Welcome to Hangman')
#drawing Hangman
playAgain = 'yes'
while playAgain == 'yes':
    def Head(tu):
        tu.ht()
        tu.forward(80)
        tu.right(90)
        tu.forward(50)
        tu.penup()
        tu.goto(55,-76)
        tu.pendown()
        tu.circle(25)
    def hlfBody(tu):
        tu.penup()
        tu.goto(80,-100)
        tu.pendown()
        tu.forward(40)
    def rightArm(tu):
        tu.left(90)
        tu.forward(50)
    def leftArm(tu):
        tu.backward(100)
        tu.forward(50)
    def fullBody(tu):
        tu.right(90)
        tu.forward(90)
    def rightLeg(tu):
        tu.left(45)
        tu.forward(80)
    def leftLeg(tu):
        tu.backward(80)
        tu.right(90)
        tu.forward(80)
    #calling the function to make drawing work
    Head(turtle)
    hlfBody(turtle)
    rightArm(turtle)
    leftArm(turtle)
    fullBody(turtle)
    rightLeg(turtle)
    leftLeg(turtle)

    user1 = input('Enter a word:')
    user1.lower()

    def guessing(user,tu):
        li = list(user)
        guess = input('Guess a letter: ').lower()
        totalGuesses = 6
        count = 0
        while True: 
            if guess in li:
                
                li.remove(guess)
                print("You've guessed one right.")
                
                if len(li) == 0:
                    print("You've guessed all of the words.")
                    tu.reset()
                    print('Do you want to play again?')
                    playAgain = input()
                    break
                guess = input('Guess another letter').lower()
                

                
                
            else:
                count+=1
                if count == 1:
                    for i in range(3):
                        tu.undo()
                elif count == 2:
                    for i in range(1):
                        tu.undo()
                elif count == 3:
                    for i in range(2):
                        tu.undo()
                elif  count == 4:
                    for i in range(3):
                        tu.undo()
                elif count == 5:
                    for i in range(5):
                        tu.undo()
                else:
                    for i in range(8):
                        tu.undo()
                    if totalGuesses == count:
                        print('You lose.')
                        print('Do you want to play again?')
                        playAgain = input()
                        break    
                        
                
                print("You didn't guess correctly, try again")
                guess = input('Guess another letter').lower()
    
                    

                

                
                
                

        
            
            
        

    guessing(user1,turtle)



#While loop to see if they want to play again