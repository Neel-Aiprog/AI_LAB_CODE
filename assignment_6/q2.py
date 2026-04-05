a = [
    [2,0,0,0,1],
    [0,1,0,0,3],
    [0,3,0,1,1],
    [0,1,0,0,1],
    [3,0,0,0,3]
]

reward = [[1,4],[2,1],[4,0],[4,4]]
reward_set = set(tuple(r) for r in reward)

class Node:
    def __init__(self, state, parent=None, cost=0, collected=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.collected = collected if collected else set()


def h(node):
    remaining = [r for r in reward if tuple(r) not in node.collected]
    # basically we keep a track of the rewards we achieve and only calculate the distance from the remaining rewards
    if not remaining:
        return 0

    x, y = node.state
    return min(abs(x-r[0]) + abs(y-r[1]) for r in remaining)


def f(node):
    return node.cost + h(node)
# this basically means the node.cost is our f(n) and h(node) is our heuristitic funciton together they make the heuristic function for our a star search

class pq:
    def __init__(self):
        self.queue = []

    def push(self, node):
        self.queue.append(node)

    def pop(self):
        best = 0
        for i in range(1, len(self.queue)):
            if f(self.queue[i]) < f(self.queue[best]):
                best = i
        return self.queue.pop(best)
        

    def is_empty(self):
        return len(self.queue) == 0


def move(node):
    children = []
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    # these directions signify movement (0,1) means the agent will move down (1,0 ) means it will move right
    # (0,-1) means it will move up and (-1,0) means the agent will move left
    for dx, dy in directions:
        x = node.state[0] + dx
        y = node.state[1] + dy

        if 0 <= x < 5 and 0 <= y < 5 and a[x][y] != 1:

            new_collected = set(node.collected)

            if (x, y) in reward_set:
                new_collected.add((x, y))

            child = Node([x,y], node, node.cost + 1, new_collected)
            children.append(child)

    return children


def A_Star_search(start):
    start_node = Node(start, collected=set())

    if tuple(start) in reward_set:
        start_node.collected.add(tuple(start))

    frontier = pq()
    frontier.push(start_node)

    reached = set()
    reached.add((start[0], start[1], tuple()))

    count_node = 0

    while not frontier.is_empty():
        node = frontier.pop()
        count_node += 1

        if len(node.collected) == len(reward):
            return node, count_node

        for child in move(node):
            state_id = (
                child.state[0],
                child.state[1],
                tuple(sorted(child.collected))
            )

            if state_id not in reached:
                reached.add(state_id)
                frontier.push(child)

    return None, count_node

def print_path(node):
    path = []
    while node:
        path.append(tuple(node.state))
        node = node.parent
    path.reverse()
    print("Path:", path)
# this function is for printing path 

def main():
    start = [0,0]

    result, explored = A_Star_search(start)

    if result:
        print(" Path found")
        print_path(result)
        print("Cost:", result.cost)
        print("Nodes explored:", explored)
    else:
        print(" No path found")

if __name__ == "__main__":
    main()