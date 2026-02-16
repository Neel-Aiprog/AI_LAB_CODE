class st:
    def __init__(self):
        self.st = []
    def push(self, data):
        self.st.append(data)
    def pop(self):
        return self.st.pop()
    def is_empty(self):
        return len(self.st) == 0
# this is stack data strcuture implemented manually in python
class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
# here node has 4 members state,action,parent and the depth of the tree
def dls(problem, limit):
    frontier = st()
    start = Node(problem["initial"], depth=0)
    frontier.push(start)
    result = "failure" #initialized the result with failure
    explored_count = 0

    while not frontier.is_empty():
        node = frontier.pop()
        print(node.state)
        explored_count += 1     # maintaining the count of  states explored
        # testing for goal
        if node.state == problem["goal"]:
            return node, explored_count
        if node.depth == limit:
            result = "cutoff"
            continue
        # Expand children
        children = expand(problem, node)
        for child in children:
            if not cycle(child):
                frontier.push(child)
    return result, explored_count
def ids(problem):
    depth = 0
    total_explored = 0
    while True:
        result, explored = dls(problem, depth)
        total_explored += path
        if result != "cutoff":
            return result, total_explored
        depth += 1
def expand(problem, node):
    g, b, boat = node.state
    children = []
    # (girls, boys) moved in boat
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    # this moves represent like this 1,0 represents 1 girl 0  boy and 0,1 represent 0 girl 1 boy 
    for x, y in moves:
        if boat == 0:        # left → right
            new_g = g - x
            new_b = b - y
            new_boat = 1
        else:                # right → left
            new_g = g + x
            new_b = b + y
            new_boat = 0
        if new_g < 0 or new_b < 0 or new_g > 3 or new_b > 3:
            continue
        girls_right = 3 - new_g
        boys_right = 3 - new_b
        if (new_g > 0 and new_b > new_g):
            continue
        if (girls_right > 0 and boys_right > girls_right):
            continue
        new_state = (new_g, new_b, new_boat)
        child = Node(
            new_state,
            parent=node,
            action=(x, y),
            depth=node.depth + 1
        )
        children.append(child)
    return children
def cycle(node):
    current_state = node.state
    parent = node.parent
    while parent is not None:
        if parent.state == current_state:
            return True
        parent = parent.parent
    return False
def path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    for state in path:
        print(state)
problem = {
    "initial": (3, 3, 0),   # (girls_left, boys_left, boat_side)
    "goal": (0, 0, 1)
}#this is the problem dictioniary 
print("Depth Limited Search")
limit = 3
result, explored = dls(problem, limit)
if result == "cutoff":
    print("Cutoff occurred")
elif result == "failure":
    print("No solution found")
else:
    print("Solution found:")
    path(result)
print("Explored states:", explored)
print("\nIterative Deepening Search")
result, explored = ids(problem)
if result == "failure":
    print("No solution found")
else:
    print("Solution found:")
    path(result)
print("Explored states:", explored)
# so here we can see that depth limited search is exploring less states than iterative deepening search as ids explores states many times at each level and dls just explores than once
# other than that ids is better than dls in this case as it is giving answer plus it has the bfs optimality and dfs memory space constraint.
# the time complexity for dls in this case is O(b^l) where b is the branching factor  number of children per node and l is the limit
# and the time complexity for ids in this  case is O(b^d) where b is branching factor and d is the depth of the shallowest goal