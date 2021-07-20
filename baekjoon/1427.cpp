#include <stdio.h>

int main(void)
{
    char numbers[11];
    scanf("%s",numbers);
    for (int i = 0; numbers[i+1] != 0; i++)
    {
        for (int j = 0; numbers[j+1] != 0; j++)
        {
            if (numbers[j] - '0' < numbers[j+1] - '0')
            {
                int temp = numbers[j];
                numbers[j] = numbers[j+1];
                numbers[j+1] = temp;
            }
        }    
    }
    printf("%s",numbers);
}