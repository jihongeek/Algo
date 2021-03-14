#include <stdio.h>
#include <algorithm>

using namespace std;

int main(void)
{
    int testcase;
    scanf("%d",&testcase);
    while (testcase--)
    {
        int n;
        int sticks[10000];
        int max = 0;
        
        scanf("%d",&n);

        for (int i = 0; i<n ; i++)
        {
            scanf("%d",&sticks[i]);
        }

        sort(sticks,sticks+n);

        for (int i = n-1; i >= 2; i--)
        {
            if (sticks[i] < sticks[i-1] + sticks[i-2])
            {
                max = sticks[i] + sticks[i-1] + sticks[i-2];
                break;    
            }
        }
        printf("%d\n",max);    
    }
}