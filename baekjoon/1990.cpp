#include <stdio.h>

int m,n,count,num;
int numbers[100000000];

void thesieve()
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
    int nums[10];
    int isPelindrome;
    scanf("%d %d",&m,&n);
    thesieve();
    int count;
    for (int i = 2;i<=n;i++)
    {
        isPelindrome = 0;
        count = -1;
        if(numbers[i]!=0 && numbers[i]>=m)
        {
            num = numbers[i];
            for (int j = 0;num!=0;j++)
            {
                nums[j]  = num % 10;
                num = num / 10;
                count++;
            }
            if (count == 0)
            {
                printf("%d\n",numbers[i]);
            }
            else
            {
                for (int k = 0; k<=count; k++)
                {
                    if (nums[k] == nums[count-k])
                    {
                        isPelindrome = 1;
                    }
                    else
                    {
                        isPelindrome = 0;
                    }
                }
                if (isPelindrome == 1)
                {
                    printf("%d\n",numbers[i]);
                }
            }
        }
    }
    printf("-1\n");
}