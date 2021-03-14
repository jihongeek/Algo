#include <stdio.h>
#define MAX_I 1000
int main(void){
    int c,n,aa,total;
    double avg;
    int ns[MAX_I];
    scanf("%d",&c);
    while (c--)
    {
        aa = 0;
        total = 0;
        scanf("%d",&n);
        for (int i = 0; i<n;i++)
        {
            scanf("%d",&ns[i]);
            total = total + ns[i];
        }
        avg = (double)total / (double)n;
        for (int i = 0; i<n;i++)
        {
            if (avg < ns[i])
            {
                aa = aa + 1;
            }
        }
        printf("%.3lf%%\n",((double)aa/(double)n)*100);
    }
}