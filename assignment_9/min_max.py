import math

board=[" " for i in range(9)] 
nodes=0

def print_board():
    print(board)
def check_Winner(bd,player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]           
    ]
    for pos in win_positions:
        if(bd[pos[0]]==bd[pos[1]]==bd[pos[2]]== player): #so it works like if there is O in all the winning positions in the board and it matches with our symbol then it is the winner
            return True
    return False
def check_draw(bd):
    return " " not in bd #if there is no space to fill for the player the game has ended in a draw
def board_str(bd):
    return "".join([c if c != " " else "-" for c in bd])
def minimax(bd, depth, is_max):
    global nodes
    nodes += 1

    indent = "   " * depth  # tree indentation

    # Terminal states
    if check_Winner(bd, "O"):
        print(f"{indent}O wins (+1) → {board_str(bd)}")
        return 1
    if check_Winner(bd, "X"):
        print(f"{indent}X wins (-1) → {board_str(bd)}")
        return -1
    if check_draw(bd):
        print(f"{indent}Draw (0) → {board_str(bd)}")
        return 0

    if is_max:
        print(f"{indent}MAX node (AI)")
        best = -math.inf

        for i in range(9):
            if bd[i] == " ":
                bd[i] = "O"
                print(f"{indent}Try O at {i} → {board_str(bd)}")

                score = minimax(bd, depth + 1, False)

                bd[i] = " "
                best = max(best, score)

                print(f"{indent}Backtrack O at {i}, score={score}, best={best}")

        return best

    else:
        print(f"{indent}MIN node (Player)")
        best = math.inf

        for i in range(9):
            if bd[i] == " ":
                bd[i] = "X"
                print(f"{indent}Try X at {i} → {board_str(bd)}")

                score = minimax(bd, depth + 1, True)

                bd[i] = " "
                best = min(best, score)

                print(f"{indent}Backtrack X at {i}, score={score}, best={best}")

        return best
def best_move():
    global nodes
    best_score=-math.inf
    move=-1
    nodes=0
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(board,0,False)
            board[i]=" "
            if score>best_score:
                best_score=score
                move=i
    print(f"nodes explored:{nodes}")
    return move
def play():
    print("TIC TAC TOE")
    print("You are X AI is O") 
    
    print_board()
    while True:
        pos=int(input("enter position(1-9):"))-1
        if(board[pos]!=" "):
            print("INVALID MOVE")
            continue
        board[pos]="X"
        print_board()
        if(check_Winner(board,"X")):
            print("you win")
            break
        if(check_draw(board)):
            print("draw")
            break
        
        ai_move=best_move()
        board[ai_move]="O"
        print("AI played:",ai_move+1) 
        print_board()
        
        if(check_Winner(board,"O")):
            print("AI WINS")
            break
        if(check_draw(board)):
            print("draw")
            break             
play()
# now if we want to visualize this game tree it will be too big as it has too many states 9! states soo if we think at every step
# if it is our AIs turn it will first check that if it has won or not or that if it is a draw or not then it will check for empty boxes and will simulate the move and it will recursively call minmax for the moves after that that is first the player will move then the ai then the player until there are no more moves left to play
# and that is when we return the best score and it will go back to its original call and keep going back to its root from where we first called it 
# and check if the score is greater than best_score then we update the best_score and move
# we also keep backtracking after every call.....because we are just making the tree not filling the board 
