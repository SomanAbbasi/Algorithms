

#BFS -> (Desperate) "First check nearly 0 distance neighbour then  1 distance , then 2 distance and so on
#  using FIFO principle"

"""
  Resource -> https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/

Given a undirected graph represented by an adjacency list adj, 
where each adj[i] represents the list of vertices connected to vertex i. 
Perform a Breadth First Search (BFS) traversal starting from vertex 0,
visiting vertices from left to right according to the adjacency list,
and return a list containing the BFS traversal of the graph.

"""

# =========BFS on Connected Graph ==========
from collections import deque

def BFS(adj):
    #no of vertices
    
    n=len(adj)
    res=[] #Store a Traversal
    idx=0
    visited=[False]*n
    q=deque()
    visited[idx]=True
    q.append(idx)
    while q:
        #Dequeue a vertex from q and store it.
        curr=q.popleft()
        res.append(curr)
        
        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)
    
    return res

if __name__=='__main__':
    adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    results=BFS(adj)
    print("==========BFS on Connected Graph========== ")
    for result in results:
        print(result,end=' ')
        



# =========BFS on Disconnected Graph ==========

"""
In a disconnected graph, not all nodes are reachable from one source.
So, BFS starting from one node will only visit the connected component that includes that node.
To ensure all nodes are visited in a disconnected graph, you use BFS multiple times, 
once for each unvisited node.

"""


def bfsOfGraph(adj,idx,visited,res):
    
    q=deque()
    visited[idx]=True
    q.append(idx)
    while q:
        curr=q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)
    return res



def bfsDisconnected(adj):
    n=len(adj)
    res=[]
    visited=[False]*n
    
    for i in range(n):
        if not visited[i]:
            bfsOfGraph(adj,i,visited,res)
    
    return res

if __name__=='__main__':
    adj =[[1, 2], [0], [0],
        [4], [3, 5], [4]]
    results=bfsDisconnected(adj)
    print()
    print()
    print("===========BFS on Disconnected Graph=======")
    for result in results:
        print(result,end=' ')


