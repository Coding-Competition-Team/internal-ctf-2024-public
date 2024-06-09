#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000 //10^9 chosen as "infinity"

int n, m, q, s, temp1, temp2, temp3;
vector<vector<pair<int, int>>> adjlist;

//dijkstra's algorithm to find single-source shortest path in a weighted graph, where weights are non-negative
//returns two vectors: shortest distance of each node from source, and predecessor of each node's shortest path from source
vector<int> dijkstra() { //takes in adjlist and source node
    // int n = adjlist.size();
    vector<int> d(n, INF); //distance from source
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;

    d[s] = 0;
    q.push(make_pair(0, s));
    while(!q.empty()) {
        int v = q.top().second;
        int dv = q.top().first;
        // cout << v << " " << dv << "\n";
        q.pop();
        if(dv!=d[v]) {
            continue;
        }

        for(size_t i=0;i<adjlist[v].size();i++) {
            int next = adjlist[v][i].first;
            int len = adjlist[v][i].second;

            if(d[v] + len < d[next]) {
                d[next] = d[v] + len;
                q.push(make_pair(d[next], next));
            }
        }
    }

    return d;
}


int main() {
    cin >> n >> m;

    adjlist.resize(n);
    for(int i=0;i<m;i++) {
        cin >> temp1 >> temp2 >> temp3;
        adjlist[temp1].push_back(make_pair(temp2, temp3));
        // adjlist[temp2].push_back(make_pair(temp1, temp3));
    }

    vector<int> d = dijkstra();
    // for(int i=0;i<n;i++) {
    //     for(int j=0;j<adjlist[i].size();j++) {
            // cout << i << " " << adjlist[i][j].first << " " << adjlist[i][j].second << "\n";
        // }
        // cout << d[i] << " ";
    // }
    // cout << "\n";

    if(d[temp1]==INF) {
        cout << -1;
    }
    else {
        cout << d[n-1];
    }
}