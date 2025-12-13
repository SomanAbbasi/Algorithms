INF = 10**15   # Large enough to avoid overflow for all practical constraints

def floyd_warshall(dist):
    """
    Computes all-pairs shortest paths.
    
    Parameters:
    dist (list[list[int]]): 
        dist[i][j] is the initial distance from i to j
        - 0 for i == j
        - edge weight if direct edge exists
        - INF if no direct edge

    Returns:
    dist (list[list[int]]):
        Updated distance matrix with shortest paths
    """
    
    V = len(dist)

    # Try each vertex as an intermediate
    for k in range(V):
        # Try improving paths from i to j using k
        for i in range(V):
            # Optimization: skip if i -> k is unreachable
            if dist[i][k] == INF:
                continue

            for j in range(V):
                # Skip if k -> j is unreachable
                if dist[k][j] == INF:
                    continue

                # Relaxation
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist

    return dist


def has_negative_cycle(dist):
    """
    Detects negative cycles after Floyd–Warshall.
    If dist[i][i] < 0 for any i, a negative cycle exists.
    """
    for i in range(len(dist)):
        if dist[i][i] < 0:
            return True
    return False


if __name__ == "__main__":
    INF = 10**15

    dist = [
        [0, 4, INF, 5, INF],
        [INF, 0, 1, INF, 6],
        [2, INF, 0, 3, INF],
        [INF, INF, 1, 0, 2],
        [1, INF, INF, 4, 0]
    ]

    floyd_warshall(dist)

    if has_negative_cycle(dist):
        print("Negative cycle exists")
    else:
        for row in dist:
            print(*row)




"""        INF = 100000000

def floydWarshall(dist):
    V=len(dist)
    
    
    # i ---> k --> j
    
    for k in range(V):
        
        
        for i in range(V):
            
            for j in range(V):
                
                if dist[i][k]!=INF and dist[k][j]!=INF:
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    
    return dist
                










if __name__ == "__main__":
    
    INF = 100000000;
    dist = [
        [0, 4, INF, 5, INF],
        [INF, 0, 1, INF, 6],
        [2, INF, 0, 3, INF],
        [INF, INF, 1, 0, 2],
        [1, INF, INF, 4, 0]
    ]
    
    floydWarshall(dist)
    for i in range(len(dist)):
        for j in range(len(dist)):
            print(dist[i][j], end=" ")
        print()
        
        
"""