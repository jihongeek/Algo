#include <stdio.h>
#define MAX_I 14
int people[MAX_I];
int peopleunder[MAX_I];
int main(void){
    int k,n,t;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d",&k);
        scanf("%d",&n);
        for (int i = 0; i < n;i++)
        {
            peopleunder[i] = i + 1;
        }
        for (int i = 0; i < k;i++)
        {
            for (int j = 0; j < n; j++)
            {
                for (int o = 0; o<j+1;o++)
                {
                    people[j] = people[j] + peopleunder[o];
                }
            }   
            for (int j = 0; j < n; j++)
            {
                peopleunder[j] = people[j];
            }   
            for (int j = 0; j < n; j++)
            {
                people[j] = 0;
            }   
        }
        printf("%d\n",peopleunder[n-1]);
    }
    
}