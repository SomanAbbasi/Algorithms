
from collections import defaultdict,deque

"""
https://www.geeksforgeeks.org/dsa/topological-sorting/
"""


def topologicalSortUtil(node, graph, visited, result):
    visited[node]=True
    
    # Recur for all adjacent vertices
    for nbr in graph[node]:
        if not visited[nbr]:
            topologicalSortUtil(nbr,graph,visited,result)
    
    
    # Push current vertex to stack which stores the result
   #result.append(node)
    result.insert(0,node)
    


def topologicalSort(V,Edges):
    graph=defaultdict(list)
    for s,t in Edges:
        graph[s].append(t)
        
    visited=[False]*V
    result=[]
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i,graph,visited,result)
    
    
   #return result[::-1]  
    return result
   
        



if __name__ == '__main__':
    # Graph represented as an adjacency list
    v = 6
    edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]

    ans = topologicalSort(v, edges)

    print(" ".join(map(str, ans)))
    


"""
from collections import defaultdict

"""
#DFS based Topological Sort with cycle detection
"""

def dfs(node, graph, state, result):
    state[node] = 1  # mark as visiting
    
    for nbr in graph[node]:
        if state[nbr] == 1:   # back edge found → cycle
            return False
        if state[nbr] == 0:   # unvisited
            if not dfs(nbr, graph, state, result):
                return False
    
    state[node] = 2  # mark as fully processed
    result.insert(0, node)  # insert at front (no reverse needed)
    return True


def topologicalSort(V, Edges):
    graph = defaultdict(list)
    for s, t in Edges:
        graph[s].append(t)
        
    state = [0] * V   # 0=unvisited, 1=visiting, 2=visited
    result = []
    
    for i in range(V):
        if state[i] == 0:
            if not dfs(i, graph, state, result):
                return []   # cycle detected → no topo sort
    
    return result
   

if __name__ == '__main__':
    v = 6
    edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]

    ans = topologicalSort(v, edges)

    if not ans:
        print("Cycle detected! No topological ordering possible.")
    else:
        print("Topological Sort Order:", " ".join(map(str, ans)))




"""