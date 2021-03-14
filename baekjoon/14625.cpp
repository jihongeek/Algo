#include <stdio.h>

int main(void)
{
    int h1, m1,h2,m2 ,n ,sliced_h,cnt;
    
    scanf("%d %d", &h1,&m1);
    scanf("%d %d", &h2,&m2);
    scanf("%d", &n);

    for (int i = h1; i<=h2; i++)
    {
        
        int j = 0;
        int k = 59;

        if (i == h1)
        {
            j = m1;
        }
        
        if (h1 == h2)
        {
            k = m2;   
        } 
        else if (i == h2)
        {
            j = 0;
            k = m2;
        }

        for (j;j<=k;j++)
        {
            if (j == n)
            {
                cnt++;
            }
            else
            {
                int sliced_h = j;
                while (sliced_h) {
                    if (sliced_h % 10 == n) {
                        cnt++;
                        break;
                    }
                    sliced_h /= 10;
                }
            }
        }
    }

    printf("%d\n",cnt);
}