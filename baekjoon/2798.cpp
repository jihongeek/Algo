#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main(void){
    int nums[101];
    int n,m,sum,max;
    scanf("%d %d",&n,&m);
    for (int i = 0;i<n;i++)
    {
        scanf("%d",&nums[i]);
    }
    sort(nums,nums+n);
    max = 0;
    sum = 0;
    for (int i = 0; i<n; i++)
    {
        if (n == 1)
        {
            max = nums[i];
            break;
        }
        for (int j = i+1; j<n; j++)
        {
            sum = nums[i] + nums[j]; 
            if (n == 2)
            {
                max = sum;
                break;   
            }
            for (int k = j+1; k<n;k++)
            {
                if (sum > m)
                {
                    break;
                }
                else if (sum + nums[k] > m)
                {
                    break;   
                }
                else if (max < sum + nums[k])
                {
                    max = sum + nums[k];
                }
            }
        }
    }
    printf("%d\n",max);
}