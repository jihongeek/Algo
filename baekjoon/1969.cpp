#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char tmp[51];
char dna[1000][51];
int HDsum[1000];
int inttmp;
int main(void)
{
    int n,m;

    scanf("%d %d", &n, &m);
    for (int i = 0; i<n; i++)
    {
        scanf("%s",dna[i]);        
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < m; k++)
            {
                if (i == j) continue;
                if (dna[i][k] != dna[j][k])
                {
                    HDsum[i]++;
                }
            }
        }    
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (HDsum[j] > HDsum[j+1])
            {
                strcpy(tmp, dna[j]);
                strcpy(dna[j],dna[j+1]);
                strcpy(dna[j+1],tmp);
                
                inttmp = HDsum[j];
                HDsum[j] = HDsum[j+1];
                HDsum[j+1] = inttmp; 
            }
            else if (HDsum[j] == HDsum[j+1])
            {
                if (strcmp(dna[j],dna[j+1]) == -1)
                {
                    strcpy(tmp, dna[j]);
                    strcpy(dna[j], dna[j + 1]);
                    
                    strcpy(dna[j + 1], tmp);
                    
                    inttmp = HDsum[j];
                    HDsum[j] = HDsum[j + 1];
                    HDsum[j + 1] = inttmp;
                }
            }

        }
    }
    printf("%d\n%s",HDsum[0],dna[0]);    
    
}