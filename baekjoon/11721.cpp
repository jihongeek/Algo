#include <stdio.h>


char word[100];
int main(void)
{
    scanf("%s",word);
    for (int i = 0;word[i]; i++)
    {
        printf("%c",word[i]);
        if(!((i+1)%10))
        {
            printf("\n");
        }
    }
}