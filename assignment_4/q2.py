grid=[
    [1, 1, 1, 1, 1, 1 , 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 'E'],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 'S', 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1 , 1]
]


start=(4, 1)
goal=(2, 7)


class pq:
    def __init__(self):
        self.queue=[]

    def push(self, node):
        self.queue.append(node)

    def pop(self):
        best=0
        for i in range(1, len(self.queue)):
            if f(self.queue[i], goal)<f(self.queue[best], goal):
                best=i
        return self.queue.pop(best)

    def is_empty(self):
        return len(self.queue)==0


class Node:
    def __init__(self, state, action, parent=None, cost=0):
        self.state=state
        self.parent=parent
        self.action=action
        self.cost=cost


def f(node, goal):
    return node.cost


def expand(problem, node):
    s=node.state
    children=[]

    moves=[(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        s0=(s[0]+dx, s[1]+dy)

        if 0<=s0[0]<len(problem) and 0<=s0[1]<len(problem[0]):
            
            if problem[s0[0]][s0[1]]!=1:
                cost=node.cost+1
                child=Node(s0, (dx,dy), node, cost)
                children.append(child)

    return children


def best_fs(problem, start, goal):

    node=Node(start, None, None, 0)

    frontier=pq()
    frontier.push(node)
    reached={start: node}
    explored_count=0

    while frontier:
        node=frontier.pop()
        explored_count+=1

        if node.state==goal:
            return node, explored_count
        
        for child in expand(problem, node):
            s=child.state

            if s not in reached or child.cost<reached[s].cost:
                reached[s]=child
                frontier.push(child)

    return None, explored_count

def extract_path(node):
    path=[]
    while node:
        path.append(node.state)
        node=node.parent
    return path[::-1]

def main():
    result_node, explored=best_fs(grid, start, goal)

    if result_node:
        path=extract_path(result_node)
        print("Evacuation Path:", path)
        print("Steps Taken:", result_node.cost)
        print("Nodes Explored:", explored)
    else:
        print("Failure")        

if __name__=='__main__':
    main()  