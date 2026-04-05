# so we want to implement the first question with cities now in simple best first search we used to expand that node at each level according to the evaluation function f(n) 
# but in greedy best first search at each level we expand according to the heuristic function basically f(n)=h(n)
# now heuristic function is basically our distance from each city to goal city kind of like a straight line distance it is to be noted
# that this distance is calculated based on the real world geographic locations and distances so these cant be predicted and they will be always given in the question
# now lets first implemenet greedy best first search it is a informed heuristic search now it is greedy so it doesnt care about the path cost
# all it cares is how fast it can get to the solution so it may not be optimal in all cases and in finite state space it may work the best but in infinite state spaces it can falter
# so lets start implementing
cities=[
    "Syracuse", "Buffalo", "Detroit", "Cleveland", "Pittsburgh", 
    "Columbus", "Indianapolis", "New York", "Philadelphia", 
    "Baltimore", "Providence", "Boston", "Portland", "Chicago"
]


graph=[
#  Sy  Bu  De  Cl  Pi  Co  In  NY  Ph  Ba  Pr  Bo  Po  Ch
 [ 0, 150, 0, 0, 0, 0, 0, 254, 253, 0, 0, 312, 0, 0],  # Syracuse
 [150, 0, 256, 189, 215, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Buffalo
 [ 0, 256, 0, 169, 0, 0, 0, 0, 0, 0, 0, 0, 0, 283],  # Detroit
 [ 0, 189, 169, 0, 134, 144, 0, 0, 0, 0, 0, 0, 0, 345],  # Cleveland
 [ 0, 215, 0, 134, 0, 185, 0, 0, 305, 247, 0, 0, 0, 0],  # Pittsburgh
 [ 0, 0, 0, 144, 185, 0, 176, 0, 0, 0, 0, 0, 0, 0],  # Columbus
 [ 0, 0, 0, 0, 0, 176, 0, 0, 0, 0, 0, 0, 0, 182],  # Indianapolis
 [254, 0, 0, 0, 0, 0, 0, 0, 97, 0, 181, 215, 0, 0],  # New York
 [253, 0, 0, 0, 305, 0, 0, 97, 0, 101, 0, 0, 0, 0],  # Philadelphia
 [ 0, 0, 0, 0, 247, 0, 0, 0, 101, 0, 0, 0, 0, 0],  # Baltimore
 [ 0, 0, 0, 0, 0, 0, 0, 181, 0, 0, 0, 50, 0, 0],  # Providence
 [312, 0, 0, 0, 0, 0, 0, 215, 0, 0, 50, 0, 107, 0],  # Boston
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 107, 0, 0],  # Portland
 [ 0, 0, 283, 345, 0, 0, 182, 0, 0, 0, 0, 0, 0, 0]   # Chicago
]

h = {
    0: 260,   # Syracuse
    1: 400,   # Buffalo
    2: 610,   # Detroit
    3: 550,   # Cleveland
    4: 470,   # Pittsburgh
    5: 640,   # Columbus
    6: 780,   # Indianapolis
    7: 217,   # New York
    8: 270,   # Philadelphia
    9: 360,   # Baltimore
    10: 50,   # Providence
    11: 0,    # Boston
    12: 107,  # Portland
    13: 860   # Chicago
}
class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state=state
        self.parent=parent
        self.cost=cost

def h1(node):
    return h[node.state]
    # here we can see earlier we used to return cost but now we return the heuristic value of that nodes
def f(node):
    return h[node.state]+node.cost
# this is for a* search which is basically heuristic + path cost
class pq:
    def __init__(self):
        self.queue=[]

    def push(self, node):
        self.queue.append(node)

    def pop_bfs(self):
        best=0
        for i in range(1, len(self.queue)):
            if h1(self.queue[i])<h1(self.queue[best]):
                best=i
        return self.queue.pop(best)
    def pop_a_star(self):
        best=0
        for i in range(1, len(self.queue)):
            if f(self.queue[i])<f(self.queue[best]):
                best=i
        return self.queue.pop(best)
    def is_empty(self):
        return len(self.queue)==0


def expand(node):
    children=[]
    for j in range(len(cities)):
        if graph[node.state][j]!=0:
            child=Node(
                j, 
                node, 
                node.cost+graph[node.state][j]
            )
            children.append(child)
    return children



def greedy_best_first_search(start, dest):
    start_node=Node(start)
    frontier=pq()
    frontier.push(start_node)
    reached=[None]*len(cities)
    reached[start]=start_node  
    global count_node
    count_node=0
    # print("Node explored", "Path cost")

    while not frontier.is_empty():
        node=frontier.pop_bfs()
        count_node+=1
        # print(f"{cities[node.state]:^15} {node.cost:^5}")

        if node.state==dest:
            return node

        for child in expand(node):
            s=child.state
            if reached[s] is None or child.cost<reached[s].cost:
                reached[s]=child
                frontier.push(child)

    return None
def A_Star_search(start, dest):
    start_node=Node(start)
    frontier=pq()
    frontier.push(start_node)
    reached=[None]*len(cities)
    reached[start]=start_node  
    global count_node
    count_node=0
    # print("Node explored", "Path cost")

    while not frontier.is_empty():
        node=frontier.pop_a_star()
        count_node+=1
        # print(f"{cities[node.state]:^15} {node.cost:^5}")

        if node.state==dest:
            return node

        for child in expand(node):
            s=child.state
            if reached[s] is None or child.cost<reached[s].cost:
                reached[s]=child
                frontier.push(child)

    return None
def print_path(node):
    path=[]
    while node:
        path.append(cities[node.state])
        node=node.parent
    path.reverse()
    print(" → ".join(path))


def main():
    start=cities.index("Chicago")
    dest=cities.index("Boston")

    result1=greedy_best_first_search(start, dest)

    if result1:
        # print("Path found:")
        print("Greedy best first search")
        print_path(result1)
        # print("Minimmum path cost:", result.cost)
        print("Nodes explored:",count_node)
    else:
        print("No path found")
    result2=A_Star_search(start, dest)
    print("A star Search")
    if result2:
        # print("Path found:")
        print_path(result2)
        # print("Minimmum path cost:", result.cost)
        print("Nodes explored:",count_node)
    else:
        print("No path found")

  


if __name__=='__main__':
    main()
# time complexity of greedy best first search is O(b^m) and time complexity of a star search is O(b^d) where b is the branching factor and m is the maximum depth of the search tree and d is the depth of the optmial solution tree
  