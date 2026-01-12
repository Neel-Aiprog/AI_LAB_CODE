def dfsRec(graph, visited, s, res):
    visited.add(s)
    res.append(s)


    # here it recursively finds vertices until the end and if they are not visited it checks them and appends them into the result
    for i in graph[s]:
        if i not in visited:
            dfsRec(graph, visited, i, res)


def dfs(graph):
    visited =set()
    res = []
    # here it loops through all vertices
    for i in graph:
        if i not in visited:
            dfsRec(graph, visited, i, res)
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
path=dfs(graph)
print(path)