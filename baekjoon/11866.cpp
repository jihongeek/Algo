#include <stdio.h>
#include <queue>

using namespace std;

int main(void)
{
    int n,k,index;
    int josephus[1000];
    queue <int> q;
    scanf("%d %d",&n,&k);
    for (int i = 1; i<=n; i++)
    {
        q.push(i);
    }

    while (!q.empty())
    {
        for (int i = 0; i < k-1; i++)
        {
            q.push(q.front());    
            q.pop();
        }
        josephus[index++] = q.front();
        q.pop();
    }
    printf("<");   
    for (int i = 0; i<n; i++)
    {
        if (i == n-1)
        {
            printf("%d",josephus[i]);
        }
        else
        {
            printf("%d, ",josephus[i]);
        }
        
    }
    printf(">");   
}