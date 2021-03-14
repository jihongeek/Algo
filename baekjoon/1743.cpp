#include <stdio.h>
#include <queue>
#include <algorithm>

using namespace std;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

bool visited[101][101];
int n,m,k; 
int map[101][101];
int groups[101*101];
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
    scanf("%d %d %d",&n,&m,&k);
    for (int i = 0; i<k ;i++)
    {
        int input_x;
        int input_y;

        scanf("%d %d",&input_x,&input_y);
        map[input_x-1][input_y-1] = 1;
    }

    for (int y = 0; y<n ;y++)
    {
        for (int x = 0; x<m; x++)
        {
            if (map[y][x] == 1 && visited[y][x] == false)
            {
                group_id++;
                bfs(y,x);
            }
        }
    }

    sort(groups + 1, groups + group_id + 1);
    
    printf("%d\n",groups[group_id]);
}