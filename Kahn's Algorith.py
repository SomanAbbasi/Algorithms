
from collections import defaultdict,deque

"""
https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/

TOPLOGICAL SORT USING BFS
"""


def topologicalSort(V,Edges):
    graph=defaultdict(list)
    inDegree=[0]*V
    for s,t in Edges:
        graph[s].append(t)
        inDegree[t]+=1 #Calculating inDegree of every Node
    
    # Queue to store vertices with indegree 0
    q=deque([i for i in range(V) if inDegree[i]==0])
    
    topoOrder=[]
    while q:
        node=q.popleft()
        topoOrder.append(node)
        for nbr in graph[node]:
            inDegree[nbr]-=1
            if inDegree[nbr]==0:
                q.append(nbr)
    
    #Check for Cycle
    if len(topoOrder)!=V:
        print("Graph Contains Cycle ")
        return []

    return topoOrder
    
        




if __name__ == "__main__":
    V = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    result = topologicalSort(V, edges)
    if result:
        print("Topological Order:", result)