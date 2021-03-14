#include <stdio.h>

int n,m,now_x,now_y,boardcolor,isSurrounded,count,input;
int board[51][102];
int boardrepaint[51][51];
int xmove[4] = {-1, 1, 0, 0};
int ymove[4] = {0, 0, -1, 1};

int repaint(void)
{
    for (int y = 0; y<8; y++)
    {
        for (int x = 0; x<8; x++)
        {
            now_x = 0;
            now_y = 0;
            boardcolor = boardrepaint[y][x];
            isSurrounded = 0;
            for (int i = 0; i<4; i++)
            {
                now_x = x + xmove[i];
                now_y = y + ymove[i];
               
                if (now_y < n && now_x < m && now_x >=0 && now_y >= 0)
                {
                    if (boardrepaint[now_y][now_x] == boardcolor)
                    {
                        isSurrounded = 1;
                    }
                    else
                    {
                        isSurrounded = 0;
                        break;
                    }
                }
            }

           if (isSurrounded == 1)
           {
               if (boardcolor == 66)
               {
                   boardrepaint[y][x] = 87;
               }
               else if (boardcolor == 87)
               {
                   boardrepaint[y][x] = 66;
               }
               count++;
           } 
        
        
        }
    }
    return count;
}

int main(void)
{
    scanf("%d %d\n",&n,&m);
    for (int y = 0; y<n; y++)
    {
        scanf("%s",&board[y]);
    }
    for (int i = 0; n - i >= 8; i++)
    {
        for (int j = 0; m - j >= 8; j++)
        {
            boardrepaint[i][j] = board[i][j];  
        }
    }
    printf("%d",count);
}