

def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] ==' '


def printBoard(board):
    print(" --- --- --- ")
    print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |   ")
    print(" --- --- --- ")
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |   ")
    print(" --- --- --- ")
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |   ")
    print(" --- --- --- ")


def isWinner(bo, le):

# Win conditions:
    return bo[0:3]==[le,le,le] or bo[3:6]==[le,le,le] or bo[6:9]==[le,le,le] or (bo[0],bo[3],bo[6])==(le,le,le) or (bo[1],bo[4],bo[7])==(le,le,le) or (bo[2],bo[5],bo[8])==(le,le,le)  or (bo[0],bo[4],bo[8])==(le,le,le) or (bo[2],bo[4],bo[6])==(le,le,le)


def isBoardFull(board):
    if board.count(" ")>1:
        return False
    else:
        return True


def playerMove():
    run=True
    
    while run:
        move = input("Where You want to put \'X\' \n  (0-8): >>>  " )
        
        try:
            move = int(move)
            print(move)
            
            if move < 9:
    
                if spaceIsFree(move):
                    insertLetter( "X", move)
                    run=False
    
                else:
                    print("this place is occupied - select another one")
    
            else:
                print("You picked not a (0-8) number  ")
                
        except:
            print("not a number")
            

def pcMove():

    possibleMoves = [ind for ind, letter in enumerate(board) if letter==" " and ind in range(0,9)]    
    move=10

    for let in ["O", 'X']:

        for i in possibleMoves:
            boardCopy= board[:]
            boardCopy[i] = let

        
            if isWinner(boardCopy,let):
                move=i
                return move

    cornersOpen = []

    for i in possibleMoves:

        if i in [0,2,6,8]:
            cornersOpen.append(i)

    if len(cornersOpen)>0:
        move = selectRandom(cornersOpen)
        return move
    
    if 4 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    
    for i in edgesOpen:
    
        if i in [1,3,5,7]:
            edgesOpen.append(i)
    
    if len(cornersOpen)>0:
        move = selectRandom(edgesOpen)
    return move


def selectRandom(li):
    
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def main():
    
    print("Lets start the game. Your turn")
    printBoard(board)

    while not (isBoardFull(board)):
    
        if not (isWinner(board,"O")):
            playerMove()
            printBoard(board)
    
        else:
            print("Sorry, O's won this time")
            break

        if not (isWinner(board,"X")):
            move =pcMove()
    
            if move == 10:
                print("Tie Game!")
                break
    
            else:
                insertLetter( "O", move)
                print(f"Computer placed O in pos: {move}")
                printBoard(board)
                
        else:
            print("X's won this time. Good Job")
            break

    if isBoardFull(board):
        print("Its Tie")
    


while True:
    
    board = [' ' for x in range(9)]
    menu = input("Welcome to Tic Tac Toe game! \n\n >>> press 'S' to START <<< \n\n >>> press 'Q' to QUIT <<< \n \n >>>")
    menu = menu.lower()

    if menu == "s":
        main()

    elif menu =="q":
        print("See You till next time!")
        quit()

    else:
        print("dupa")



