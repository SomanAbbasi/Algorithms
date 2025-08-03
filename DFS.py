

# DFS from a Given Source of Undirected Graph: "ADJACENCY MATRIX"
# Referecne: https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/

# ======== DFS on Connected Graph ==========

def dfsRecursion(adj,visited,source,res):
    visited[source]=True
    res.append(source)
    
    for neighbour in range(len(adj)):
        if not visited[neighbour] and adj[source][neighbour]==1:
            dfsRecursion(adj,visited,neighbour,res)
    return res


def DFS(adj):
    visited=[False]*len(adj)
    results=[]
    dfsRecursion(adj,visited,0,results)
    return results


def add_edge(adj,s,t):
    adj[s][t]=1
    adj[t][s]=1
    

V=5 #Total number of vertices ->  the highest-numbered vertex + 1,
#If the highest node is 4, the total number of vertices is 5 (nodes: 0, 1, 2, 3, 4)

adj=[[0]*V for _ in range(V)]

edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

for s,t in edges:
    add_edge(adj,s,t)

res=DFS(adj)
for r in res:
    print(r,end=' ')




# ========= DFS on Disconnected Graph ===========

#Adjaency list version

def dfs_Recursion(adj,visited,idx,res):
    visited[idx]=True
    res.append(idx)
    for i in adj[idx]:
        if not visited[i]:
            dfs_Recursion(adj,visited,i,res)
            
    return res


def dfs(Adj):
    visited=[False]*len(Adj)
    res=[]
    for i in range(len(Adj)):
        if not visited[i]:
            dfs_Recursion(Adj,visited,i,res)
            
    
    
    return res

def Add_Edges(adj,s,t):
    Adj[s][t]=1
    Adj[t][s]=1
    


v=6
Adj=[[0]*v for _ in range(v)]

Edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
for s,t in Edges:
    Add_Edges(adj,s,t)

print()
print()
print("DFS Traversal for Disconnected Graph")
results=dfs(Adj)
for r in results:
    print(r,end=' ')



""""
✅ 1. DFS using Adjacency Matrix

👉 For Connected Graph:

def dfs_connected_matrix(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfs_connected_matrix(adj, visited, i, res)

# Example usage
adj = [
    [0, 1, 1, 0],  # connections from node 0
    [1, 0, 0, 0],  # node 1
    [1, 0, 0, 1],  # node 2
    [0, 0, 1, 0]   # node 3
]
n = len(adj)
visited = [False] * n
res = []
dfs_connected_matrix(adj, visited, 0, res)
print("Connected DFS (Matrix):", res)



👉 For Disconnected Graph:

def dfs_disconnected_matrix(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfs_disconnected_matrix(adj, visited, i, res)

# Wrapper to handle all components
def dfs_full_matrix(adj):
    n = len(adj)
    visited = [False] * n
    res = []
    for i in range(n):
        if not visited[i]:
            dfs_disconnected_matrix(adj, visited, i, res)
    return res

# Example usage
adj = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
]
print("Disconnected DFS (Matrix):", dfs_full_matrix(adj))



"""

"""

✅ 2. DFS using Adjacency List
👉 For Connected Graph:

def dfs_connected_list(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    for neighbor in adj[s]:
        if not visited[neighbor]:
            dfs_connected_list(adj, visited, neighbor, res)

# Example usage
adj = {
    0: [1, 2],
    1: [0],
    2: [0, 3],
    3: [2]
}
n = len(adj)
visited = [False] * n
res = []def dfs_disconnected_list(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    for neighbor in adj[s]:
        if not visited[neighbor]:
            dfs_disconnected_list(adj, visited, neighbor, res)

def dfs_full_list(adj):
    n = len(adj)
    visited = [False] * n
    res = []
    for i in range(n):
        if not visited[i]:
            dfs_disconnected_list(adj, visited, i, res)
    return res

# Example usage
adj = {
    0: [1],
    1: [0],
    2: [3],
    3: [2]
}
print("Disconnected DFS (List):", dfs_full_list(adj))

dfs_connected_list(adj, visited, 0, res)
print("Connected DFS (List):", res)



👉 For Disconnected Graph:





"""