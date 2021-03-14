#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <utility>
using namespace std;
int cvs[105][105];
int festival[2], home[2];
int visited[105][105];

int isVisited(int xNow, int yNow, int cvsNum)
{
    for (int i = 0; i < cvsNum; i++)
    {
        if (visited[i][0] == xNow && visited[i][1] == yNow)
        {
            return 1;
        }
    }
    return 0;
}

int bfs(int y, int x, int cvsNum)
{
    int beer = 20;
    int isHappy = 0;
    int index = 0;;
    int lastLocation[2] = {x,y};
    queue < pair<int, int> > q;
    q.push(make_pair(x,y));
    while(!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        int len = abs(x - lastLocation[0]) + abs(y - lastLocation[1]); 
        if (beer - (len / 50) < 0)
        {
            return isHappy;
        }
        if (abs(x - festival[0])  + abs(y - festival[1]) <= 50)
        {
            isHappy = 1;
            return isHappy;
        }
        
        
        for (int i = 0; i < cvsNum; i++)
        {

            int xNow = x + cvs[i][0];
            int yNow = y + cvs[i][1];
            
            if (!isVisited(xNow,yNow,cvsNum))
            {
                visited[index][0] = xNow;
                visited[index][1] = yNow;
                index++;
                q.push(make_pair(xNow, yNow));
                lastLocation[0] = x;
                lastLocation[1] = y;
            }
        }
    }
    return isHappy;
}

int main(void)
{
    int testcase, cvsNum;
    scanf("%d",&testcase);    
    
    while(testcase--)
    {
        scanf("%d",&cvsNum);
        scanf("%d %d",&home[0],&home[1]);
        for (int i = 0; i < cvsNum; i++)
        {
            scanf("%d %d",&cvs[i][0],&cvs[i][1]);
        }
        scanf("%d %d",&festival[0],&festival[1]);
        printf("%d",bfs(home[1] , home[0], cvsNum));
    }
}