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
        
