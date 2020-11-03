#include <stdio.h>
#include <stdlib.h>

int nuke[] = {'A','C','G','T'};
int nuke_nums[] = {0,0,0,0};
char answer_dna[51];
char dna[1000][51];
int HDsum;
int max_n,max;

int main(void)
{
    int n,m;

    scanf("%d %d", &n, &m);
    for (int i = 0; i<n; i++)
    {
        scanf("%s",dna[i]);        
    }
    
    for (int i = 0; i < m; i++)
    {
        max_n = 0;
        max = 0;
        for (int j = 0; j < 4; j++)
        {
            nuke_nums[j] = 0;
        }
        for (int j = 0; j < n; j++)
        {
            if (dna[j][i] == 'A') nuke_nums[0]++;               
            if (dna[j][i] == 'C') nuke_nums[1]++;
            if (dna[j][i] == 'G') nuke_nums[2]++;               
            if (dna[j][i] == 'T') nuke_nums[3]++;               
        }    
        for (int j = 0; j < 4; j++)
        {
            if (nuke_nums[j] > max)
            {
                max_n = nuke[j];
                max = nuke_nums[j];
            }
        }
        answer_dna[i] = max_n;    

    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (answer_dna[j] != dna[i][j])
            {
                HDsum++;
            }
        }
    }
    printf("%s\n%d",answer_dna,HDsum);    
}