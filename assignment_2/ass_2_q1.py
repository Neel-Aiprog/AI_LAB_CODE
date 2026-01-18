class queue():
    def __init__(self):
        self.arr=[]
    def add_front(self,ele):
        self.arr.insert(0,ele)
    def add_rear(self,ele):
        self.arr.append(ele)
    def remove_front(self):
        return self.arr.pop(0)
    def remove_rear(self):
        return self.arr.pop()              
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

def bfs_8_puzzle_problem(i_state, f_state):
    Queue = queue()
    visited = set()
    explore = 0

    Queue.add_rear(i_state)
    visited.add(to_tuple(i_state))

    while Queue:
        state = Queue.remove_front()
        explore += 1

        if state == f_state:
            return explore

        for neighbor in next_states(state):
            t = to_tuple(neighbor)
            if t not in visited:
                visited.add(t)
                Queue.add_rear(neighbor)

    return -1

initial_state = [[7,2,4],[5,0,6],[8,3,1]]
final_state   = [[0,1,2],[3,4,5],[6,7,8]]

print(bfs_8_puzzle_problem(initial_state, final_state))
