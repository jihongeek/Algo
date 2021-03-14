#include <stdio.h>
#include <queue>

using namespace std;

int dx[] = {-1, 0, 1, 0, 1, -1, 1, -1};
int dy[] = {0, 1, 0, -1, 1, 1, -1, -1};

bool visited[50][50];
int w,h; 
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

        for (int i = 0; i<8; i++)
        {
            int now_x = x + dx[i];
            int now_y = y + dy[i];
            
            if (now_x >= 0 && now_x < w && now_y >= 0 && now_y < h)
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
    while (1)
    {
        group_id = 0;
        scanf("%d %d",&w,&h);

        if (w == 0 && h == 0)
        {
            break;
        }
        for (int i = 0; i<h; i++)
        {
            for (int j = 0; j<w; j++)
            {
                scanf("%1d",&map[j][i]);
            }

        }

        for (int i = 0; i<h ;i++)
        {
            for (int j = 0; j<w; j++)
            {
                if (map[j][i] == 1 && visited[j][i] == false)
                {
                    group_id++;
                    bfs(j,i);
                }
            }
        }
        for (int i = 0; i<w ;i++)
        {
            for (int j = 0; j<h; j++)
            {
                map[i][j] = 0;
                visited[i][j] = false;
            }
        }
        for (int i = 0; i<w*h; i++)
        {
            groups[i] = 0;
        }
        printf("%d\n",group_id);
    }

    
}