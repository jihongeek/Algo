#include <stdio.h>
#include <queue>
using namespace std;
int main(void){
    queue <int> q,sq;
    int imp,t,n,where,max;
    scanf("%d",&t);
    while(t--)
    {
        imp = 0;
        n = 0;
        where = 0;
        max = 0;
        scanf("%d %d",&n,&where);
        for (int i = 0;i<n;i++)
        {
            scanf("%d",&imp);
            if (max < imp)
            {
                max = imp;
            }
            q.push(imp);   
        }
        for (int i = 0;i<n;i++)
        {
            if (q.front()>max)
            {
                q.push(q.front());
                q.pop();   
            }
            else
            {
                q.pop()    
            }
            
        }
    }
}