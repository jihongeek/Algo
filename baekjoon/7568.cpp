#include <stdio.h>

int main(void)
{
    int n,weight[50],height[50],grade;
    scanf("%d",&n);
    for (int i = 0; i<n;i++)
    {
        scanf("%d %d",&weight[i],&height[i]);
    }
    for (int i = 0; i<n;i++)
    {
        grade = 0;
        for (int j = 0;j<n;j++)
        {
            if (weight[i] < weight[j] && height[i] < height[j])
            {
                grade++;
            }
        }
        printf("%d ",grade+1);
    }
}