#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;


int anums[100000];
int xnums[100000];

int main(void)
{
    int n,m,anum;
    scanf("%d",&n);
    for (int i  = 0; i < n; i++)
    {
        scanf("%d", &anums[i]);
    }
    sort(anums,anums + n);
    scanf("%d",&m);


    for (int i  = 0; i < m; i++)
    {
        scanf("%d", &xnums[i]);
    }
    for (int i  = 0; i < m; i++)
    {
        int left = 0,right = n-1;
        int isFind = 0;
        while (left <= right)
        {
            int mid  = (left + right)/ 2;
            if (xnums[i] == anums[mid])
            {
                isFind = 1;
                break;
            }
            else if (xnums[i] > anums[mid])
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;   
            }
        }
        printf("%d\n",isFind);
    }
}