#include <stdio.h>

char room[101][101];
int main(void)
{
    int n,cnt,row,col;
    row = 0;
    cnt = 0;
    col = 0;
    scanf("%d",&n);
    for (int i = 0; i<n; i++)
    {
        scanf("%s",&room[i]);    
    }

    for (int i = 0; i<n; i++)
    {
        cnt = 0;
        for (int j = 0; j<n; j++)
        {
            if (room[i][j] == 88)
            {
                if (cnt >= 2) row++;
                cnt = 0;
            }
            else cnt++;
        }
        if (cnt >= 2) row++; 
    }
    for (int i = 0; i<n; i++)
    {
        cnt = 0;
        for (int j = 0; j<n; j++)
        {
            if (room[j][i] == 88)
            {
                if (cnt >= 2) col++;
                cnt = 0;
            }
            else cnt++;
        }
        if (cnt >= 2) col++; 
    }
    printf("%d %d",row,col);
}