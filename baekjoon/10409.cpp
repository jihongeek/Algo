#include <stdio.h>

int n,t,sum,ans;
int worktimes[101];

int main(void)
{
    scanf("%d %d",&n,&t);
    for (int i = 0; i<n; i++)
    {
        scanf("%d",&worktimes[i]);
        sum = sum + worktimes[i];
        if (sum > t)
        {
            break;
        }
        ans = i+1;        
    }
    printf("%d",ans);
}