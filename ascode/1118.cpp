#include <stdio.h>
#include <stdlib.h>

using namespace std;

#include <algorithm>

int ms[1500000], ns[10000], m,n,cnt;
int main(void)
{
    scanf("%d %d", &m,&n);
    for (int i = 0; i<m; i++)
    {
        scanf("%d", &ms[i]);
    }
    sort(ms,ms+1500000);
    for (int i = 0; i<n; i++)
    {
        scanf("%d", &ns[i]);
    }
    sort(ns,ns+10000);

    for (int i = 10000 - n; i<10000; i++)
    {
        int left = 1499999 - m;
        int right = 1499999;
        int mid = (left + right) / 2;
        while (left <= right)
        {
            mid = (left+right)/2;
            if (ns[i] == ms[mid])
            {
                cnt++;
                break; 
            }
            else if (ns[i] > ms[mid])
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
    }
    printf("%d\n",cnt);
    
}