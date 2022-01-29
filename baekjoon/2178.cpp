#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <tuple>

using namespace std;

int n,m;
vector <string> maze;
bool visited[100][100];


bool is_valid(int row, int col) 
{
    if (row < 0 || row >= n) 
    {
        return false;
    }
    if (col < 0 || col >= m) 
    {
        return false;
    }
    if (visited[row][col])
    {
        return false;
    }
    if (maze[row][col] != '1')
    {
        return false;
    }
    return true;
}

int move(int row,int col)
{
    queue <tuple<int,int,int>> q; 
    visited[row][col] = true;
    q.push(make_tuple(row,col,1));
    while (!q.empty())
    {
        int row = get<0>(q.front());
        int col = get<1>(q.front());
        int dist = get<2>(q.front());
        q.pop();
        if (row == n - 1 and col == m - 1) return dist;

        if (is_valid(row-1,col))
        {
            visited[row-1][col] = true;
            q.push(make_tuple(row-1,col,dist+1));
        }
        if (is_valid(row+1,col))
        {
            visited[row+1][col] = true;
            q.push(make_tuple(row+1,col,dist+1));
        }
        if (is_valid(row,col-1))
        {
            visited[row][col-1] = true;
            q.push(make_tuple(row,col-1,dist+1));
        }
        if (is_valid(row,col+1))
        {
            visited[row][col+1] = true;
            q.push(make_tuple(row,col+1,dist+1));
        }
    }
}

int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        string line;
        cin >> line;
        maze.push_back(line);   
    }
    cout << move(0,0) << "\n";
    
}