#include <stdio.h>

char castle[51][51];
int col[51];
int row[51];
int main(void)
{
    int n,m;
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++)
    {
        scanf("%s",castle[i]);
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (castle[i][j] == 88)
            {
                row[i]++;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (castle[j][i] == 88)
            {
                col[i]++;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m && row[i]; j++)
        {
            if (col)
        }
    }
    

}