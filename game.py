board = ["  " for i in range (9)] # this prints out 9 separated spaces, it would print out like : " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2]) 
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
# Every row was defined in order to see a tick tack toe board printed and also it is placed a format to input the number while playing the game


    print()
    print(row1)
    print(row2)
    print(row3)
    print()

#the first and last print function is just for stetic view while row 1, 2 and 3 print function would show us the board by itself

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    
    print("Your turn player {}".format(number))

    choice = int(input("Enter your move (1-9): ").strip()) # we had to convert the argument into a integer "int" because inputs would be numbers
    if board[choice - 1] == "  ":
        board[choice - 1] = icon #We had to put a -1 in order to put the "x" in the correct place for instance if we type 8 and we dont have the -1 argument it would show the "x" in 9 position according to python programming
    else:
        print()
        print("That place is taken!")

#here we define the winning rules by returning a true or false statement in order to win the game, starting by rows, columns and last with diagonals
def is_victory(icon):
    if (board[0] == icon and board [1] == icon and board [2] == icon) or \
       (board[3] == icon and board [4] == icon and board [5] == icon) or \
       (board[3] == icon and board [4] == icon and board [5] == icon) or \
       (board[0] == icon and board [3] == icon and board [6] == icon) or \
       (board[1] == icon and board [4] == icon and board [7] == icon) or \
       (board[2] == icon and board [5] == icon and board [8] == icon) or \
       (board[0] == icon and board [4] == icon and board [8] == icon) or \
       (board[2] == icon and board [4] == icon and board [6] == icon):
        return True
    else:
        return False
    
def is_draw():#if the game is a draw and there is no space left we tell our program to check it inside "board" be a "True" otherwise be a "false" statement
    if "  " not in board:
        return True
    else:
        return False
    
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw(): #here is where if its true or false it would run the condition "elif"
        print("Its a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw(): #here is where if its true or false it would run the condition "elif"
     print("Its a draw!")
     break
        
    
        
    
     
