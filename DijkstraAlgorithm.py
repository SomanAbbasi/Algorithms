
""""

     ==> Step-by-Step Implementation <==

SOURCES: https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/

=> Set dist[source]=0 and all other distances as infinity.
=> Push the source node into the min heap as a pair <distance, node> → i.e., <0, source>.
=> Pop the top element (node with the smallest distance) from the min heap.
=> For each adjacent neighbor of the current node:
   * Calculate the distance using the formula:
        => dist[v] = dist[u] + weight[u][v]
    If this new distance is shorter than the current dist[v], update it.
        => Push the updated pair <dist[v], v> into the min heap
Repeat step 3 until the min heap is empty.
Return the distance array, which holds the shortest distance from the source to all nodes.
"""
import heapq
from collections import defaultdict
def Dijkstra(n,edges,src):
    graph=defaultdict(list)
    for s,t,w in edges:
        graph[s].append((t,w))
        graph[t].append((s,w)) #Remove if graph is directed
    
    dist=[float("inf")]*n
    dist[src]=0
    #Min-heap priority queue
    pq=[(0,src)]
    while pq:
        d,u=heapq.heappop(pq)
        #Skip Outdated entreis
        if d>dist[u]:
            continue
        
        for v,w in graph[u]:
            new_dist=dist[u]+w
            if new_dist<dist[v]:
                dist[v]=new_dist
                heapq.heappush(pq,(dist[v],v))
        
    
    return dist

n = 5
edges = [
    (0, 1, 2), (0, 2, 4),
    (1, 2, 1), (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]
src = 0

print(Dijkstra(n, edges, src))