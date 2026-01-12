from collections import deque
def BFS_all_paths(graph, src, dest):
    q = deque([[src]])
    all_paths = []
    while q:
        path = q.popleft()
        node = path[-1]
        # here it is using a doubly ended queue 

        if node == dest:
            all_paths.append(path)
            continue
        # it is to be noted that in bfs it is updating all paths subseuquently according to the neighbours of the current source
        
        for nei,_ in graph[node]:
            if nei not in path:
                q.append(path + [nei])
                # here it is updating the path in the result

    return all_paths
def path_cost(graph, path):
    cost = 0
    for i in range(0,len(path)-1):
        for nei, w in graph[path[i]]:
            if nei == path[i+1]:
                cost += w
    return cost
    # it is to calculate cost of all the paths that are calculated and appended in the result matrix
# this is our main graph where we configured each and every point
graph = {
    "Syracuse": [("Buffalo",150),("Boston",312),("New York",254),("Philadelphia",253)],
    "Buffalo": [("Syracuse",150),("Detroit",256),("Cleveland",189),("Pittsburgh",215)],
    "Detroit": [("Buffalo",256),("Chicago",283)],
    "Cleveland": [("Buffalo",189),("Chicago",345),("Pittsburgh",134),("Detroit",169),("Columbus",144)],
    "Pittsburgh": [("Buffalo",215),("Cleveland",134),("Columbus",185),("Baltimore",247),("Philadelphia",305)],
    "Columbus": [("Pittsburgh",185),("Indianapolis",176),("Cleveland",144)],
    "Indianapolis": [("Columbus",176),("Chicago",182)],
    "New York": [("Syracuse",254),("Philadelphia",97),("Providence",181),("Boston",215)],
    "Philadelphia": [("New York",97),("Baltimore",101),("Pittsburgh",305),("Syracuse",253)],
    "Baltimore": [("Philadelphia",101),("Pittsburgh",247)],
    "Providence": [("New York",181),("Boston",50)],
    "Boston": [("Syracuse",312),("Providence",50),("Portland",107)],
    "Portland": [("Boston",107)],
    "Chicago": []}
paths = BFS_all_paths(graph, "Syracuse", "Chicago")

for p in paths:
    print(p, "=>", path_cost(graph, p))
