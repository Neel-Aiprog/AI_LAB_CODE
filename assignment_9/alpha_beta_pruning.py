import math

board=[" " for i in range(9)] 
nodes=0
global pruned
pruned=0
def print_board():
    print(board)
def check_Winner(bd,player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]           
    ]
    for pos in win_positions:
        if(bd[pos[0]]==bd[pos[1]]==bd[pos[2]]== player):
            return True
    return False
def check_draw(bd):
    return " " not in bd
def print_board_inline(bd):
    return "".join([c if c != " " else "-" for c in bd])

def minimax(bd, depth, is_max, alpha, beta):
    global nodes, pruned
    nodes += 1

    indent = "   " * depth  # for tree structure

    # Terminal states
    if check_Winner(bd, "O"):
        print(f"{indent}O wins → +1 | {print_board_inline(bd)}")
        return 1
    if check_Winner(bd, "X"):
        print(f"{indent}X wins → -1 | {print_board_inline(bd)}")
        return -1
    if check_draw(bd):
        print(f"{indent}Draw → 0 | {print_board_inline(bd)}")
        return 0

    if is_max:
        best = -math.inf
        print(f"{indent}MAX node | α={alpha}, β={beta}")

        for i in range(9):
            if bd[i] == " ":
                bd[i] = "O"
                print(f"{indent}Try O at {i}")

                score = minimax(bd, depth + 1, False, alpha, beta)

                bd[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)

                print(f"{indent}Backtrack O at {i} → score={score}, best={best}")

                if beta <= alpha:
                    print(f"{indent}PRUNE at MAX (α={alpha} ≥ β={beta})")
                    pruned += 1
                    break

        return best

    else:
        best = math.inf
        print(f"{indent}MIN node | α={alpha}, β={beta}")

        for i in range(9):
            if bd[i] == " ":
                bd[i] = "X"
                print(f"{indent}Try X at {i}")

                score = minimax(bd, depth + 1, True, alpha, beta)

                bd[i] = " "
                best = min(best, score)
                beta = min(beta, best)

                print(f"{indent}Backtrack X at {i} → score={score}, best={best}")

                if beta <= alpha:
                    print(f"{indent}🔥 PRUNE at MIN (β={beta} ≤ α={alpha})")
                    pruned += 1
                    break

        return best
def best_move():
    global nodes
    nodes=0
    best_score=-math.inf
    move=-1
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(board,0,False,-math.inf,math.inf)
            board[i]=" "
            if score>best_score:
                best_score=score
                move=i
    print(f"nodes explored {nodes}")
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
print(f"nodes pruned:{pruned}")
# alpha beta pruning is a optimisation of the min max algorithm and it works in the way like at each call it has two extra variables 
# alpha and beta and if beta<= alpha that branch is pruned soo alpha variable is the best score that maximiser(ai) can gurantee upto that level  and beta is best score that player can limit ai to that is minimiser function() 
# soo at any step beta drops below alpha we know that the AI is getting a better score else where then it will not further explore that subtree and hence prune it

