from collections import deque

def bfs_connected(graph, src, visited, res):
    q = deque()
    visited.add(src)
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)
        # here also we use doubly ended queue
        # and here also bfs explores level by level and it first finds source appends it and then finds the neighbours and appends them eventually forming the bfs tree
        for x in graph[curr]:
            if x not in visited:
                visited.add(x)
                q.append(x)


def bfs(graph):
    visited = set()
    res = []

    for node in graph:
        if node not in visited:
            bfs_connected(graph, node, visited, res)
            # to check if any node is not visited then it would call the bfs_connected to find its corresponding tree

    return res


# this is our graph
graph = {
        "Raj": ["Sunil", "Neha_1"],
        "Sunil": ["Raj", "Akash", "Sneha", "Maya"],
        "Akash": ["Sunil", "Priya"],
        "Priya": ["Raj", "Akash", "Aarav"],
        "Neha_1": ["Raj", "Akash", "Sneha", "Aarav"],
        "Sneha": ["Sunil", "Rahul", "Neha_1"],
        "Maya": ["Sunil", "Rahul", "Arjun_1"],
        "Rahul": ["Sneha", "Maya", "Pooja", "Arjun_2", "Neha_2", "Neha_1"],
        "Arjun_1": ["Maya", "Pooja"],
        "Pooja": ["Arjun_1", "Rahul", "Arjun_2"],
        "Arjun_2": ["Rahul", "Aarav", "Neha_2"],
        "Neha_2": ["Rahul", "Aarav", "Arjun_2", "Neha_1", "Priya"],
        "Aarav": ["Neha_1", "Neha_2", "Arjun_2"]
    }
path=bfs(graph)
print(path)