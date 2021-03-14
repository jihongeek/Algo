#include <stdio.h>
#define MAX_I 100000
int main(void){
    int testcase,a,b,ba,bb,PN,k;
    int primes[MAX_I];
    scanf("%d",&testcase);
    while(testcase--){
        PN = 0;
        scanf("%d %d",&a, &b);
        for (int i = a; i<b+1;i++)
        {
            for (int j = 2; j<i; j++)
            {
                if (j != a && i%j==0)
                {
                    break;
                }
                primes[k] = i;
                k = k + 1;
            }
        }
        for (int i = 0,i<k;i++)
        {
            
        }
    }
}