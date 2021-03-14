#include <stdio.h>
#include <queue>
using namespace std;

int visited[1001][1001];
int box[1001][1001];
int h,w,cnt;
int xmove[] = {-1,1,0,0};
int ymove[] = {0,0,1,-1};
queue <pair<int,int>> q;  
int bfs()
{
    int x,y;
    int ret = 1;
    
    while(!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (int i = 0; i<4; i++)
        {
            int now_x = x + xmove[i]; 
            int now_y = y + ymove[i];
            if (now_x < w && now_y < h && now_x >= 0 && now_y >= 0)
            {
                if (box[now_y][now_x] == -1)
                {
                    continue;
                }
                if (box[now_y][now_x] == 0 && !visited[now_y][now_x])
                {
                    visited[now_y][now_x] = 1;
                    box[now_y][now_x] = box[y][x] + 1;
                    q.push({now_x,now_y});
                }
            }
        }
    }
    ret = box[y][x] - 1;
    for (int i = 0; i<h; i++)
    {
        for (int j = 0; j<w; j++)
        {
            if (box[i][j] == 0)
            {
                ret = -1;
                break;  
            }
        }
    }
    return ret;
}

int main(void)
{
    int cnt;
    scanf("%d %d",&w,&h);
    for (int y = 0; y<h; y++)
    {
        for (int x = 0; x<w; x++)
        {
            scanf("%d",&box[y][x]);
        }
    }
    
    for (int y = 0; y<h; y++)
    {
        for (int x = 0; x<w; x++)
        {
            if (box[y][x] == 1 && visited[y][x] == 0)
            {
                visited[y][x] = 1;
                q.push({x, y});
            }
        }
    }
    cnt = bfs();

    printf("%d\n",cnt);
}