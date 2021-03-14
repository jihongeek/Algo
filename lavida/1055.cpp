#include <stdio.h>

int main(void)
{
    int digit[] = {128, 64, 32, 16, 8, 4, 2, 1};
    char binaryIp[33];
    int sum;
    int testcase;
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%s",binaryIp);
        for (int i = 0; i < 4; i++)
        {
            sum = 0;
            for (int j = 0; j < 8; j++)
            {
                if (binaryIp[i * 8 + j] == '1')
                {
                    sum += digit[j];
                }
            }
            if (i < 3)
            {
                printf("%d.", sum);
            }
            else
            {
                printf("%d\n", sum);
            }
        }
    }
}