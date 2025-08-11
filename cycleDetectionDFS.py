"""
========Undirected Graph Cycle========

https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
"""


from typing import List
from collections import defaultdict
class Solution:
    def dfsTraversal(self,node,graph,visited,parent):
        visited[node]=True
        for nbr in graph[node]:
            if not visited[nbr]:
                ans=self.dfsTraversal(nbr,graph,visited,node)
                if ans:
                    return True
            elif visited[nbr] and nbr!=parent:
                return True
        
        return False
                
    def isCycle(self, V, edges):
         visited=[False]*V
         graph=defaultdict(list)
         for s,t in edges:
             graph[s].append(t)
             graph[t].append(s)
             
         #print(visited)
         for i in range(V):
             if not visited[i]:
                 ans=self.dfsTraversal(i,graph,visited,-1)
                 if ans:
                     return True
        
         return False
                 



s1=Solution()
s1.isCycle(4,[[0, 1], [0, 2], [1, 2], [2, 3]])
        
		
  
  
"""
=============Directed Graph Cycle============
https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
from collections import defaultdict

"""



class Solution:
    def isCycle(self, V, edges):
        graph=defaultdict(list)
        for s,t in edges:
            graph[s].append(t)
        visited=[False]*V
        cp=[False]*V # pathVisited
        
        def dfsTraversal(node):
            visited[node]=True
            cp[node]=True
            for nbr in graph[node]:
                if not visited[nbr]:
                    ans=dfsTraversal(nbr)
                    if ans:
                        return True
                elif cp[nbr]:
                    return True
            cp[node]=False
            return False

        for i in range(V):
            if not visited[i]:
                ans=dfsTraversal(i)
                if ans:
                    return True
                
        return False
                    

        
        
  
                
                
     
        
