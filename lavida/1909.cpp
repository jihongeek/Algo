#include <stdio.h>
#include <algorithm>

using namespace std;
int nums[100000];

int binarySearch(int x,int n)
{
    int left = 0; 
    int right = n;

    while (right - left >= 1)
    {
        int mid = (left + right) / 2;
        if (nums[mid] == x) return mid;
        else if (nums[mid] < x) left = mid + 1;
        else right = mid;
         
    }
    return -1;
}

int main(void)
{
    int testcase;
    int n,q;
    scanf("%d",&n);   
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&nums[i]);
    } 
    scanf("%d",&testcase);    
    while(testcase--)
    {
        scanf("%d",&q);
        printf("%d\n",binarySearch(q,n));
    }
}