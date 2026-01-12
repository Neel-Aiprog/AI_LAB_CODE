# lets first try to understand what is bfs
from collections import deque
def BfsConnected(adj,src,visited,res):
    q=deque()
    visited[src]=True
    q.append(src)
    
    while q:
        curr=q.popleft()
        res.append(curr)
        
        
        #visit all unvisited
        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)
def Bfs(adj):
    V=len(adj)
    visited=[False]*V
    res=[]
    
    for i in range(V):
        if not visited[i]:
            BfsConnected(adj,i,visited,res)
            
    return res
def addedge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
V=6
adj=[]
for i in range(V):
    adj.append([])
addedge(adj,1,2)
addedge(adj, 2, 0)
addedge(adj, 0, 3)
addedge(adj, 5, 4)

res = Bfs(adj)
for node in res:
    print(node," ")