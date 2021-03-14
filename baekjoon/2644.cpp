#include <stdio.h>
#include <queue>

using namespace std;
int graph[101][101];
int chonsu[101][101];
int bfs(int n, int start)
{
    int count = 0;
    queue <int> q;
    bool check[n+1] = {false};
    check[start] = true;
    q.push(start);

    while (!q.empty())
    {
        int now = q.front();
        q.pop();
        for (int i = 1; i <= n;i++)
        {
            if (graph[now][i] == 1 && !check[i])
            {
                check[i] = true;
                q.push(i);
            }
        }
    }
    for (int i=2; i<=n; i++)
    {
        if (check[i]==true)
        {
            count += 1;
        }
    }
    return count;
}

int main(void){
    int n,parent,child,m,node1,node2,infected;
    scanf("%d",&n);
    scanf("%d %d",&parent,&child);
    scanf("%d",&m);
    for (int i = 0;i<m;i++)
    {
        scanf("%d %d",&node1,&node2);
        graph[node1][node2] = 1;
        graph[node2][node1] = 1;
        
    }
    infected = bfs(n,1);
    printf("%d\n",infected);
}