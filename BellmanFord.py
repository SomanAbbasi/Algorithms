import sys

def bellmanFord(V,edges,src):
    INF=sys.maxsize
    dist=[INF]*V
    dist[src]=0
    
    for i in range(V):
        updated=False
        for edge in edges:
            u,v,w=edge
            if dist[u]!=INF and   dist[u]+w<dist[v]:
                
                # If this is the Vth relaxation, then there 
                # is a negative cycle
                if i==V-1:
                    return [-1]
                
                dist[v]=dist[u]+w
                updated=True
        if not updated:
            break
                
    return dist
    
    



if __name__ == '__main__':
    V = 5
    edges = [[1, 3, 2], 
             [4, 3, -1], [2, 4, 1], 
             [1, 2, 1],
             [0, 1, 5]]

    src = 0
    ans = bellmanFord(V, edges, src)
    print(' '.join(map(str, ans)))