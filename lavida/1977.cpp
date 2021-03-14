#include <stdio.h>

int main(void)
{
    int digit[] = {128, 64, 32, 16, 8, 4, 2, 1};
    char binaryIp[33];
    int decimalIp[4];
    int sum;
    int testcase;
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d.%d.%d.%d",&decimalIp[0],&decimalIp[1],&decimalIp[2],&decimalIp[3]);
        for (int i = 0; i < 4; i++)
        {
            for (int j = 8; j > -1; j--)
            {
                binaryIp[i*8+j] = decimalIp[i] % 2 + '0';
                decimalIp[i] = decimalIp[i] / 2;
            }
        }
        binaryIp[32] = '\0';
    }
}