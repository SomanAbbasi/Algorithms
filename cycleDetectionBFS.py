"""
========Undirected Graph Cycle========

https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
"""

from collections import defaultdict,deque


class Solution:
    def isCycle(self, V, edges):
         visited=[False]*V
         graph=defaultdict(list)
         for s,t in edges:
             graph[s].append(t)
             graph[t].append(s)
         q=deque()
         
         def bfs(node):
             q.append((node,-1))
             visited[node]=True
             while q:
                 node,parent=q.popleft()
                 for nbr in graph[node]:
                     if not visited[nbr]:
                         q.append((nbr,node))
                         visited[nbr]=True
                     elif nbr!=parent:
                         return True
             return False
         
         
         
         for i in range(V):
             if not visited[i]:
                 ans=bfs(i)
                 if ans:
                     return True
         return False
        


"""
=========Directed Graph Cycle============
https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1


from collections import defaultdict, deque

def contains_cycle_directed_bfs(V, edges):
    graph = defaultdict(list)
    indegree = [0] * V

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(V) if indegree[i] == 0])
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return processed != V  # if some nodes remain unprocessed → cycle


# Example
V = 4
edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
print(contains_cycle_directed_bfs(V, edges))  # True

V = 4
edges = [[0, 1], [1, 2], [2, 3]]
print(contains_cycle_directed_bfs(V, edges))  # False



"""