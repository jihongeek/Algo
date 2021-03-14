#include <stdio.h>

int main(void)
{
    char board[5][16] = {0,};
    
    for (int i = 0; i<5; i++)
    {
        scanf("%s",&board[i]);
    }

    for (int i = 0; i<15; i++)
    {
        for (int j = 0; j<5; j++)
        {
            if (!board[j][i]) continue;
            else printf("%c",board[j][i]);
        }
    }    
}