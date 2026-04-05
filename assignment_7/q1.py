# here we are given the 8 queens problem and we have to implement various hill climbing algorithm variants and we will compare them 
# first we will try to implement the simple hill climbing
# it works like we start from a starting randomly generated state and we caluclate its neighbours and we jump off to the best neighbour and we keep doing this in the hope of finding
# global optimum but there are issues with  this algo  as we can get stuck in the local optimum due to various issues soo lets try to solve this problem.

# we are going to define a chess board state with a list containing 8 numbers each number representing where that queen is in that indexed column
import random
import math
chessboards=[]
for i in range(50):
    board = list(range(8))  
    random.shuffle(board)   
    chessboards.append(board)
# now if we want to caluclate the heuristic we can either count the number of pairs attacking each other or we can count the number of pairs not attacking each other
# the first one should be minimum and the other one should be maximmum
def attacking(board):
    n=len(board)
    attack=0
    for i in range(0,n):
        for j in range(i+1,n):
            if(board[i]==board[j]): #for checking the rows
                attack+=1
            if(abs(i-j)==abs(board[i]-board[j])): #for checking the diagonals
                attack+=1
    return attack
def get_neighbours(board):
    neighbours=[]
    n=len(board)
    for column in range(0,n):
        for row in range(0,n):
            if(row!=board[column]):
                neighbour=board[:] #for copying the current board
                neighbour[column]=row #we are moving queen to every other row in its column
                neighbours.append(neighbour)
    return neighbours
# for caluclating a neighbour of a current board we move queen to every other row in its column
def steepest_ascent_HC(board):
    current=board[:]
    steps=0
    initial_heuristic=attacking(current)
    while True:
        current_score=attacking(current)
        
        if(current_score==0): #we minimise the number of attacking pairs
            final_heuristic=attacking(current)
            return current,steps,"GLOBAL OPTIMUM",initial_heuristic,final_heuristic
        neighbours=get_neighbours(current)
        
        best_neighbour=min(neighbours,key=attacking)
        best_score=attacking(best_neighbour)
        
        if best_score>=current_score:
            # no improvemnet stuck at local optimum
            final_heuristic=attacking(current)
            return current,steps,"LOCAL OPTIMUM",initial_heuristic,final_heuristic 
        current=best_neighbour
        steps+=1
steepest_solved=0
steepest_local=0
m=1
print("STEEPEST ASCENT HILL CLIMBING")
for board1 in chessboards:
    chess_board,steps,status,init_heuristic,final_heuristic=steepest_ascent_HC(board1)
    
    print(f"board number:{m}|board state:{chess_board}|steps:{steps}|status:{status}|intial heuristic:{init_heuristic}|final heuristic:{final_heuristic}")
    if(status=="GLOBAL OPTIMUM"):
        steepest_solved+=1
    if(status=="LOCAL OPTIMUM"):
        steepest_local+=1
    m+=1
print("=====================================================================================================================================================")\
    
def first_choice_HC(board):
    current=board[:]
    steps=0
    initial_heuristic=attacking(current)
    while True:
        current_score=attacking(current)
        if current_score==0:
            final_heuristic=attacking(current)
            return current,steps,"GLOBAL OPTIMUM",initial_heuristic,final_heuristic
        improve=False
        for i in range(125):
            row=random.randint(0,7)
            col=random.randint(0,7)
            if (row==current[col]):
                continue
            neighbour=current[:]
            neighbour[col]=row
            if(attacking(neighbour)<current_score):
                current=neighbour
                steps+=1
                improve=True
                break
        if not improve:
            final_heuristic=attacking(current)
            return current,steps,"LOCAL OPTIMUM",initial_heuristic,final_heuristic
first_local=0
m=1
first_choice_solved=0
print("FIRST CHOICE HILL CLIMBING")
for board1 in chessboards:
    chess_board,steps,status,init_heuristic,final_heuristic=first_choice_HC(board1)
    print(f"board number:{m}|board state:{chess_board}|steps:{steps}|status:{status}|intial heuristic:{init_heuristic}|final heuristic:{final_heuristic}")
    if(status=="GLOBAL OPTIMUM"):
        first_choice_solved+=1
    if(status=="LOCAL OPTIMUM"):
        first_local+=1
    m+=1
# print(f"total first_choice_solved boards:{first_choice_solved}")
# print(steepest_local,first_local)    
# print(first_choice_solved)
# random restart hill climbing
def random_restart_hc(board, max_restarts=50):
    restarts = 0
    total_steps = 0
    current = board[:]  
    
    while restarts < max_restarts:
        result, steps, status, init_h, final_h = steepest_ascent_HC(current)
        total_steps += steps
        
        if status == "GLOBAL OPTIMUM":
            return result, total_steps, "GLOBAL OPTIMUM", restarts, init_h, final_h
        

        restarts += 1
        current = list(range(8))
        random.shuffle(current)
    
    return result, total_steps, "FAILED", restarts, init_h, final_h
restart_local=0
m=1
restart_solved=0
print("==================================================================================================================================")
print("RANDOM RESTART HILL CLIMBING")
for board1 in chessboards:
    chess_board,steps,status,init_heuristic,restarts,final_heuristic3=random_restart_hc(board1)
    print(f"board number:{m}|board state:{chess_board}|steps:{steps}|status:{status}|intial heuristic:{init_heuristic}|final heuristic:{final_heuristic3}|Restarts:{restarts}")
    if(status=="GLOBAL OPTIMUM"):
        restart_solved+=1
    if(status=="FAILED"):
        restart_local+=1
    m+=1
# print(f"total solved boards:{solved3}")
# print(f"steepest_ascent_hc:{steepest_local},restart_local_hc:{restart_local},first_local_hc:{first_local}")  
print("=================================================================================================================================")
def simulated_annealing(board,T=100,cooling_rate=0.999,min_temp=0.01):
    current=board[:]
    steps=0
    init_heuristic=attacking(current)
    
    while T>min_temp:
        current_score=attacking(current)
        
        if current_score==0:
            return current, steps, "GLOBAL OPTIMUM", init_heuristic, attacking(current)
        col = random.randint(0, 7)
        row = random.randint(0, 7)
        while row == current[col]:      
            row = random.randint(0, 7)

        neighbour = current[:]
        neighbour[col] = row
        neighbour_score = attacking(neighbour)
        delta=neighbour_score-current_score
        if delta<0:
            current=neighbour
        else:
            probability=math.exp(-delta/T)
            if random.random()<probability:
                current=neighbour
        T*=cooling_rate
        steps+=1
    final_heuristic = attacking(current)
    return current, steps, "LOCAL OPTIMUM", init_heuristic, final_heuristic
print("SIMULATED ANNEALING")
simulated_local=0
m=1
simulated_solved=0
for board1 in chessboards:
    chess_board,steps,status,init_heuristic,final_heuristic3=simulated_annealing(board1)
    print(f"board number:{m}|board state:{chess_board}|steps:{steps}|status:{status}|intial heuristic:{init_heuristic}|final heuristic:{final_heuristic3}")
    if(status=="GLOBAL OPTIMUM"):
        simulated_solved+=1
    if(status=="LOCAL OPTIMUM"):
        simulated_local+=1
    m+=1
# print(f"total solved boards:{simulated_solved}")
# print(f"steepest_ascent_hc:{steepest_local},restart_local_hc:{restart_local},first_local_hc:{first_local},simulated_local:{simulated_local}")
print("THE TOTAL SOLVED STATES OUT OF 50 for each algorith")
print("==SOLVED==")
print(f"STEEPEST_ACCENT_HC:{steepest_solved}")
print(f"FIRST_CHOICE_HC:{first_choice_solved}")
print(f"RANDOM_RESTART_HC:{restart_solved}")
print(f"SIMULATED ANNEALING:{simulated_solved}")
print("==LOCAL==")
print(f"STEEPEST_ACCENT_HC:{steepest_local}")
print(f"FIRST_CHOICE_HC:{first_local}")
print(f"RANDOM_RESTART_HC:{restart_local}")
print(f"SIMULATED ANNEALING:{simulated_local}")
# here in steepest ascent hc we pick the best neighbour out of all the neighbours of the current state and move to that otherwise return the current state(local optimum)
# in first choice hc we randomly generate some neighbours and pick the first best one out of them and we move to that neighbour and if we dont find any we return the current state(local optimum)
# now in the above two algorithms there are chances of getting stuck in local maximum so we have a third algorithm random restart
# if we get stuck in local maximum we restart the whole process soo in this we almost never get stuck in local maximum and therefore we find the solution to all the generated boards
# but in this method we explore a lot so sc and tc is a lot and in first choice the sc and tc is less but there are chances of getting stuck
# in simulated annealing we start with a starting temperature and caluclate a random neighour and if it is worse than the current we accept it with a probability
# of e raise to - delta / temperature so basically at high temperatures we accept more worse moves but with time we also decrease the temperature slowly
# so we settle to accepting good solutions and we also have a minimum temperature as a limiting condition
# so here we have better results than steepest ascent and first choice but still not better than random restart so in  the situation of 8 queens problem random restart hc is giving us the best solution
# simulated annealing depends on the cooling rate if we decrease the cooling rate it will explore more and more space and will eventually find the global optimum but it highly depends on the temperature
# for example for 0.99 it will solve only 30-31 states but for 0.999 it will solve all of them but it will take many steps
# basically random restart hc is doing steepest ascent hc again and again until it escapes out of local optimum