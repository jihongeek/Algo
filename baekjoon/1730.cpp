#include <stdio.h>

int board[100][100];
char cmd[1001];
int main(void)
{

    int i,x, y, n,num;
    x = 0;
    y = 0;
    num = 0;
    scanf("%d",&n);
    scanf("%s",cmd);
    
    for (i = 0; cmd[i]; i++)
    {
        num++;
    }

    for (i = 0; i<num;i++)
    {
        if (cmd[i] == 'D')
        {
            if (y + 1 == n)
            {
                continue;
            }
            if (board[y][x] == 0 || board[y][x] == '|') board[y][x] = '|';
            else board[y][x] = '+';
            y++;
            if (board[y][x] == 0 || board[y][x] == '|') board[y][x] = '|';
            else board[y][x] = '+';
        } 
        if (cmd[i] == 'U')
        {
            if (y - 1 < 0)
            {
                continue;
            }
            if (board[y][x] == 0 || board[y][x] == '|') board[y][x] = '|';
            else board[y][x] = '+';
            y--;
            if (board[y][x] == 0 || board[y][x] == '|') board[y][x] = '|';
            else board[y][x] = '+';
        } 
        if (cmd[i] == 'L')
        {
            if (x - 1 < 0)
            {
                continue;
            }
            if (board[y][x] == 0 || board[y][x] == '-') board[y][x] = '-';
            else board[y][x] = '+';
            x--;
            if (board[y][x] == 0 || board[y][x] == '-') board[y][x] = '-';
            else board[y][x] = '+';
                
        } 
        if (cmd[i] == 'R')
        {
            if (x + 1 == n)
            {
                continue;
            }
            if (board[y][x] == 0 || board[y][x] == '-') board[y][x] = '-';
            else board[y][x] = '+';
            x++;
            if (board[y][x] == 0 || board[y][x] == '-') board[y][x] = '-';
            else board[y][x] = '+';
        } 
    }
    for (i = 0; i < n; i++)
    {
        for (int j = 0; j  < n; j++)
        {
            if (board[i][j] == 0) printf(".");
            else printf("%c",board[i][j]);
        }
        printf("\n");
    }
}