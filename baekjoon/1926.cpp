#include <stdio.h>
#include <queue>
#include <utility>
using namespace std;

int rowMove[4] = {1,-1,0,0}; // 세로 
int colMove[4] = {0,0,1,-1}; // 가로 
int paper[501][501];
int visited[501][501];
int n,m;

int pictures;

int bfs(int row, int col)
{
    int area = 1;
    queue <pair<int,int>> q;
    visited[row][col] = 1;
    q.push({row,col});
    while (!q.empty())
    {
        row = q.front().first;
        col = q.front().second; 
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nowRow = row + rowMove[i];
            int nowCol = col + colMove[i];

            if (nowRow >= 0 and nowRow < n and nowCol >= 0 and nowCol < m)
            {
                if (!visited[nowRow][nowCol] and paper[nowRow][nowCol])
                {
                    visited[nowRow][nowCol] = 1;
                    area++;
                    q.push({nowRow,nowCol});
                }
            }
        }        
    }
    return area;
}

int main(void)
{
    int maxArea = 0;
    int count = 0;
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d",&paper[i][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (paper[i][j] and !visited[i][j])
            {
                count++;
                int area = bfs(i,j);
                if (area > maxArea)
                {
                    maxArea = area;
                }
            } 
        }
    }
    printf("%d\n%d",count,maxArea);
}