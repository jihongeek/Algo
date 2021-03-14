#include <stdio.h>


int bomb[10][10];
int board[10][10];
int display[10][10];

int n;
int xmove[] = {-1,1,0,0,-1,1,-1,1};
int ymove[] = {0,0,1,-1,-1,-1,1,1};

int main(void)
{
    scanf("%d\n",&n);
    for (int i = 0; i<n ; i++)
    {
        for (int j = 0; j<n; j++)
        {
            scanf("%c\n",&board[i][j]);
        }
    }
    for (int i = 0; i<n ; i++)
    {
        for (int j = 0; j<n; j++)
        {
            scanf("%c\n",&display[i][j]);
        }
    }

    for (int i = 0; i<n ; i++)
    {
        for (int j = 0; j<n; j++)
        {
            for (int k = 0; k<8; k++)
            {
                int x = j + xmove[k];
                int y = i + ymove[k];
                if (x>=0 && y>=0 && x<n && y<n)
                {
                    if (board[y][x] == 42)
                    {
                        bomb[i][j] = bomb[i][j]+1;
                    }
                }
            }
        }
    }
    for (int i = 0; i<n ; i++)
    {
        for (int j = 0; j<n+1; j++)
        {
            if (j == n)
            {
                printf("\n");
                break;
            } 
            else if (display[i][j] == 120)
            {
                printf("%d",bomb[i][j]);
            }
            else
            {
                printf(".");
            }
        }
    }
}