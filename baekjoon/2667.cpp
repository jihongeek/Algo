#include <stdio.h>
#include <queue>

using namespace std;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

bool visited[50][50];
int n,m,k,t; 
int map[50][50];
int groups[2500];
int group_id;

void bfs(int x, int y)
{
    queue < pair <int,int> > q;
    
    visited[x][y] = true;
    q.push(make_pair(x,y));
    groups[group_id]++;

    while(!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for (int i = 0; i<4; i++)
        {
            int now_x = x + dx[i];
            int now_y = y + dy[i];
            
            if (now_x >= 0 && now_x < n && now_y >= 0 && now_y < m)
            {
                if (map[now_x][now_y] == 1 && visited[now_x][now_y] == false)
                {
                    visited[now_x][now_y] = true;
                    groups[group_id]++;
                    q.push(make_pair(now_x,now_y));
                }
            } 
        }               
    }
}

int main(void)
{
    scanf("%d",&t);
    while (t--)
    {
        group_id = 0;
        scanf("%d %d %d",&n,&m,&k);

        for (int i = 0; i<k ;i++)
        {
            int x;
            int y;

            scanf("%d %d",&x,&y);
            map[x][y] = 1;   
        }

        for (int i = 0; i<n ;i++)
        {
            for (int j = 0; j<m; j++)
            {
                if (map[i][j] == 1 && visited[i][j] == false)
                {
                    group_id++;
                    bfs(i,j);
                }
            }
        }
        for (int i = 0; i<n ;i++)
        {
            for (int j = 0; j<m; j++)
            {
                map[i][j] = 0;
                visited[i][j] = false;
            }
        }
        printf("%d\n",group_id);
    }

    
}