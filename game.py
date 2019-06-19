import random
def disp_board(board):
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")

def move(board,x,y,symbol):
    if(board[x-1][y-1] == 'X' or board[x-1][y-1] == 'O' or x>3 or x<0 or y>3 or y<0):
        return False
    board[x-1][y-1] = symbol
    return True

def check_win(board):
    for i in range(3):
        sym=board[i][0]
        if(not sym == '-' and sym == board[i][1] and sym == board[i][2]):
            return True
    for i in range(3):
        sym = board[0][i]
        if(not sym == '-' and sym == board[1][i] and sym == board[2][i]):
            return True
    if(not (board[0][0] == '-' or board[1][1] == '-' or board[2][2] == '-') and board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return True
    if(not (board[0][2] == '-' or board[1][1] == '-' or board[2][0] == '-') and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return True

    return False

def main():
    play = True
    while(play):
        print("Welcome to Tic Tac Toe Game")
        board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        player1 = 'O'
        player2 = 'X'

        #sym = input("player 1 selects the symbol O/X : ") #1
        
        #if(sym == 'X' or sym == 'x'): #2
        #    player1 = 'X' #3
        #    player2 = 'O' #4

        for i in range(9):
            disp_board(board)
            if(i%2==0):
                print("Player 1 Choose Position:")
                player=player1
            else:
                print("Player 2 Choose Position:")
                player=player2

            pos = False
            while(not pos):
                #x,y = input().split() #5
                #x = int(x) #6
                #y = int(y) #7
                #Randomly Selecting positions
                x=random.randint(1,3) #8
                y=random.randint(1,3) #9
                print(x,y)
                if not move(board,x,y,player):
                    print("Invalid Position...retry")
                    pos = False
                else:
                    pos = True
            tie = 1    
            if(i>3 and check_win(board)):
                tie = 0
                if(player==player1):
                    print("Player 1 Wins")
                else:
                    print("Player 2 Wins")
                break
        if(tie == 1):
            print("Match Tie")
        disp_board(board)

        print("Retry y/n?")
        inp = input()
        if not (inp == 'y' or inp == 'Y'):
            play = False
            
    print("Thankyou") 
    

if(__name__ == '__main__'):
    main()
