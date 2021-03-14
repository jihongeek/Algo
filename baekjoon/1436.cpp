#include <stdio.h>

int n,count,count_six,divided_i;

int main(void)
{
    scanf("%d",&n);
    count = 0;
    for (int i = 666; 1;i++)
    {
        count_six = 0;
        divided_i = i;
        while (divided_i)
        {
            if (divided_i % 10 == 6)
            {
                count_six++;
            }
            else if (count_six < 3)
            {
                count_six = 0;
                divided_i = divided_i / 10;
                continue;
            }
            divided_i = divided_i / 10;
        }
        if (count_six >= 3)
        {
            count++;
        }
        if (n == count)
        {
            printf("%d\n",i);
            break;
        }
    }
}