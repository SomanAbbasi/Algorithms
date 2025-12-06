//#include <bits/stdc++.h>
#include<iostream>
#include<vector>
#include<string>
#include <queue>

using namespace std;


vector<int> shortestReach(int n, vector<vector<int>> edges, int s)
{

    vector<vector<pair<int, int>>> graph(n);
    
    

    for (int i = 0; i < edges.size(); i++)
    {
        int nbr1 = edges[i][0]-1;
        int nbr2 = edges[i][1]-1;

        int weight = edges[i][2];
        graph[nbr1].push_back({nbr2, weight});
        graph[nbr2].push_back({nbr1, weight});
    }

    vector<int> dist(n, INT_MAX);
    dist[s - 1] = 0;

    // Min heap
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
    heap.push({0, s - 1});

    while (!heap.empty())
    {
         pair<int,int> topElement=heap.top();
        heap.pop();
        int currDist=topElement.first;
        int node=topElement.second;

        if (currDist > dist[node])
        {
            continue;
        }

        for (auto &edge : graph[node])
        {
            int nbr = edge.first;
            int weight = edge.second;
            int newDist = currDist + weight;
            if (newDist < dist[nbr])
            {
                dist[nbr] = newDist;
                heap.push({newDist, nbr});
            }
        }
    }

    vector<int> res;

    for (int i = 0; i < n; i++)
    {
        if (i != s - 1)
        {
            if (dist[i] == INT_MAX)
            {
                res.push_back(-1);
            }
            else
            {
                res.push_back(dist[i]);
            }
        }
    }
    return res;
}
int main()
{
    

   

}


/*

class Solution
{
public:
    vector<int> dijkstra(int V, vector<vector<int>> &edges, int src)
    {

        vector<vector<pair<int, int>>> graph(V);

        for (int i = 0; i < edges.size(); i++)
        {
            int nbr1 = edges[i][0];
            int nbr2 = edges[i][1];
            int weight = edges[i][2];

            graph[nbr1].push_back({nbr2, weight});
            graph[nbr2].push_back({nbr1, weight});
        }

        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        priority_queue<pair<int, int>> heap; // max-heap
        heap.push({0, src});

        while (!heap.empty())
        {

            pair<int, int> topEl = heap.top();
            heap.pop();

            int currDist = -topEl.first;
            int node = topEl.second;
            if (currDist > dist[node])
            {
                continue;
            }

            for (auto &edge : graph[node])
            {
                int nbr = edge.first;
                int weight = edge.second;
                int newDist = weight + currDist;
                if (newDist < dist[nbr])
                {
                    dist[nbr] = newDist;
                    heap.push({-newDist, nbr});
                }
            }
        }
        return dist;
    }
};

*/


