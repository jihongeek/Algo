#include <stdio.h>

int p1,p2,p3,n,testcase,min;
int numbers[1000];
void thesieve(int n)
{
    for (int i = 0;i<=n;i++)
    {
        numbers[i] = i;
    }
    for (int i = 2; i <= n;i++)
    {
        if (numbers[i] == 0)
        {
            continue;
        }
        for (int j = 2 * i; j <= n; j = j + i)
        {
            if (numbers[j] == 0)
            {
                continue;
            }
            else
            {
                numbers[j] = 0;
            }
        }
    }
}

int main(void){
    scanf("%d",&testcase);
    thesieve(1000);
    int p1,p2,p3;
    while (testcase--)
    {
        int psum = 0;
        min = 1001;
        p1 = 0;
        p2 = 0;
        p3 = 0;
        scanf("%d",&n);
        for (int i = 2; i < n; i++)
        {
            if (numbers[i])
            {
                if (i > n) 
                {
                    p1 = 0;
                    break;
                }
                p1 = numbers[i];
                for (int j = 2; j<n;j++)
                {
                    if (numbers[j])
                    {
                        if (p1 + p2 + p3 == n && p3 != 0 ) break;
                        if (j > n - p1) 
                        {
                            p2 = 0;
                            break;
                        }
                        p2 = numbers[j];
                        for (int k = 2; k < n; k++)
                        {
                            if (p1 + p2 + p3 == n) break;
                            if (k > n - p1 - p2)
                            {
                                p3 = 0;
                                break;
                            }
                            if (numbers[k])
                            {
                                p3 = numbers[k];
                            }
                        }
                    }
                }
            }
        }
        if (p1 + p2 + p3 < n)
        {
            printf("-1\n");
        }
        else
        {
            printf("%d %d %d\n",p1,p2,p3);
        }
    }
}