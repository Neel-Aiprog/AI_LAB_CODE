def dfs_paths(graph, source, dest):
    paths = []

    def dfs(city, path, visited):
        if city == dest:
            paths.append(path.copy())
            return

        for neighbor, dist in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, path, visited)
                path.pop()
                visited.remove(neighbor)
                # basically our algo first goes deep into the graph and then backtracks one time and explores other paths to eventually find all paths 

    dfs(source, [source], {source}) #the firsy source is our city the second is our path and the third is our visited array so it is recursively calculating paths for us 
    return paths

# this is our graph

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

def path_cost(graph, path):
    cost = 0
    for i in range(0,len(path)-1):
        for j, w in graph[path[i]]:
            if j == path[i+1]:
                cost += w
    return cost
result=dfs_paths(graph,"Syracuse","Chicago")
for i in result:
    print(f"{i}-->",path_cost(graph,i))
