#include <stdio.h>

int n,now_x,now_y,max,peopleid;
int board[51][51];
int xmove[4] = {-1, 1, 0, 0};
int ymove[4] = {0, 0, -1, 1};
int people[2500];

void checkfriend(void)
{
    peopleid = -1;
    for (int y = 0; y<n; y++)
    {
        for (int x = 0; x<n; x++)
        {
            peopleid++;
            now_x = 0;
            now_y = 0;
            for (int i = 0; i<4; i++)
            {
                now_x = x + xmove[i];
                now_y = y + ymove[i];
               
                if (board[y][x] == 89 && now_y < n && now_x < n && now_x >=0 && now_y >= 0)
                {
                    if (board[now_y][now_x] == 89)
                    {
                        people[peopleid]++;           
                    }
                }
            }
        }
    }

}

int main(void)
{
    scanf("%d\n",&n);
    for (int y = 0; y<n; y++)
    {
        for (int x = 0; x<n; x++)
        {
            scanf("%1c\n",&board[y][x]);
        }
    }
    checkfriend();
    for (int i = 0; i<n*n; i++)
    {
        if (people[i] > max)
        {
            max = people[i];
        }
    }
    printf("%d",max);
}
