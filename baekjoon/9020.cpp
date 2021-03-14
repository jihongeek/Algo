#include <stdio.h>

int g1,g2,n,testcase,min;
int numbers[10000];
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
    thesieve(10000);
    while (testcase--)
    {
        min = 10001;
        scanf("%d",&n);
        for (int i = 2; i<n; i++)
        {
            if (n - numbers[i] == numbers[n - numbers[i]]&&(n - numbers[i]) - numbers[i] < min && (n - numbers[i]) - numbers[i] >= 0)
            {
                min = (n - numbers[i]) - numbers[i];
                g1 = numbers[i];
                g2 = n - numbers[i];
            }
        }
        printf("%d %d\n",g1,g2);
    }

}