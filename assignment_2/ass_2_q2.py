class Stack:
    def __init__(self):
        self.arr = []

    def push(self, ele):
        self.arr.append(ele)

    def pop(self):
        return self.arr.pop()

    def is_empty(self):
        return len(self.arr) == 0            
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def to_tuple(s):
    return tuple(tuple(row) for row in s)

def next_states(i_state):
    m, n = find_zero(i_state)
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbours = []

    for dx, dy in moves:
        ax, ay = m + dx, n + dy
        if 0 <= ax < 3 and 0 <= ay < 3:
            state = [list(row) for row in i_state]
            state[m][n], state[ax][ay] = state[ax][ay], state[m][n]
            neighbours.append(state)

    return neighbours
def dfs_8_puzzle_problem(i_state,f_state):
    stack=Stack()
    visited=set()
    explore=0
    stack.push(i_state)
    visited.add(to_tuple(i_state))
    while not  stack.is_empty():
        current=stack.pop() 
        explore+=1
        
        if(current==f_state):
            return explore
        for next in next_states(current):
            t=to_tuple(next)
            if t not in visited:
                visited.add(t)
                stack.push(next)
    return -1
initial_state = [[7,2,4],[5,0,6],[8,3,1]]
final_state   = [[0,1,2],[3,4,5],[6,7,8]]

print(dfs_8_puzzle_problem(initial_state, final_state))
# if we had to compare the cost according to the depth of the tree   more costlier would be dfs as even though less number of states are explored it goes as deep as it can into one branch of the tree while on the other hand bfs explores each level simulatneously hence having less cost