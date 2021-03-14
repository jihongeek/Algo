#include <stdio.h>
int main(void){
    int t,n,max_i;
    long long max;
    long long litres[100];
    char schools[20][100];
    scanf("%d",&t);
    while (t--)
    {
        max  = 0;
        scanf("%d",&n);
        for (int i = 0;i<n;i++)
        {
            scanf("%s %d",&schools[i],&litres[i]);
            if (litres[i]>max){
                max = litres[i];
                max_i = i;
            }
        }
        printf("%s\n",schools[max_i]);
    }
    
}