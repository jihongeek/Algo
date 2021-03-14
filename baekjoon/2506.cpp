#include <stdio.h>
int main(void){
    int n,score,count;
    int ox[100];
    scanf("%d",&n);
    for (int i = 0; i<n;i++)
    {
        scanf("%d",&ox[i]);
    }
    score = 0;
    count = 0;
    for (int i = 0; i<n; i++)
    {
        if (ox[i]==1){
            count = count + 1; 
        }
        else
        {
            count = 0;
        }
        score = score + count;
    }
    printf("%d\n",score);

} 