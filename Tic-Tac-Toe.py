import random
def drawBoard(board):
    #This function prints the layout out of the tic-tac-toe game board
    print('    |    |')
    print(' ' + board[7] + '  | ' + board[8] + '  |  ' + board[9])
    print('    |    |')
    print('---------------')
    print('    |    |')
    print(' ' + board[4] + '  | ' + board[5] + '  |  ' + board[6])
    print('    |    |')
    print('---------------')
    print('    |    |')
    print(' ' + board[1] + '  | ' + board[2] + '  |  ' + board[3])
    print('    |    |')

def inputPlayerLetter():
    #asking if player wants to be X or O
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


def whoGoesFirst():
    #Randomly chose the player to go first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def PlayAgain():
    #this function returns true if player wants to play again, otherwise returns false
    print('Do you want to play again ( yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #bo= board and le= letter
    return((bo[7] == le and bo[8] == le and bo[9] == le)or #across top
           (bo[4] == le and bo[5] == le and bo[6] == le) or #across middle
           (bo[1] == le and bo[2] == le and bo[3] == le) or #across buttom
           (bo[7] == le and bo[4] == le and bo[1] == le) or #down left
           (bo[8] == le and bo[5] == le and bo[2] == le) or #down middle
           (bo[9] == le and bo[6] == le and bo[3] == le) or #down right
           (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal
           (bo[9] == le and bo[5] == le and bo[1] == le)) #diagonal
    
def getBoardCopy(board):
    dupeboard = []
    for i in board:
        dupeboard.append(i)
    return dupeboard

def isSpaceFree(board, move):
    #return true if the passed move is free on passed board
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move):
        print("What's your next move? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #Here is our algorithm for out Tic Tac Toe
    #First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
    if move != None:
        return move
    #Try to take the center, if its free
    if isSpaceFree(board, 5):
        return 5
    #Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #return true when all space is occupied
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic-Tac-Toe")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gamesIsplaying = True

    while gamesIsplaying:
        if turn == 'player':
        #players turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Horray! You have won the game')
                gamesIsplaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'computer'

        else:

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! you lose.')
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player'


    if not PlayAgain():
        break










