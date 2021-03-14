#include <stdio.h>
int main(void){
    int score,n,temp,l,k,sub1[100],sub2[100];
    scanf("%d %d %d",&n,&l,&k);
    score = 0;
    for (int i = 0; i<n; i++)
    {
        scanf("%d %d",&sub1[i],&sub2[i]);
    }
    for (int i = 0; i<n; i++)
    {
        for (int j = 0; j<n-1; j++)
        {
            if (sub2[j] < sub2[j+1])
            {
                temp = sub2[j];
                sub2[j] = sub2[j+1];
                sub2[j+1] = temp;
                temp = sub1[j];
                sub1[j] = sub1[j+1];
                sub1[j+1] = temp;
            }
        }
    }
    for (int i = n-1; i>-1;i--)
    {
        if (k == 0)
        {
            break;
        }
        if (l >= sub2[i])
        {
            score = score + 140;
        }
        else if (l >= sub1[i])
        {
            score = score + 100;
        }
        else
        {
            continue;
        }
        k--;
    }
    printf("%d\n",score);
}