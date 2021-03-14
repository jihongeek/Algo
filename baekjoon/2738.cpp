#include <stdio.h>
#define MAX_R 100
#define MAX_C 100
int main(void) {
    int n, m;
    int a[MAX_R][MAX_C];
    int b[MAX_R][MAX_C];
    int c[MAX_R][MAX_C];

    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &b[i][j]);
        }
    }
    for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                c[i][j] = a[i][j] + b[i][j];
                printf("%d ", c[i][j]);
            }
            printf("\n");
        }
}