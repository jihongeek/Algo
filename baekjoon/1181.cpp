#include <stdio.h>
#include <string.h>

char words[20000][50];
char word[50];
int wordlens[20000];
int main(void)
{
    int n,tmp,isSame;
    scanf("%d",&n);
    for (int i = 0; i<n; i++)
    {
        scanf("%s",&words[i]);
        for (int j = 0; j<50; j++)
        {
            if (!words[i][j]) break;
            wordlens[i]++;
        }
    }
    for (int i =0; i<n;i++)
    {
        for (int j = 0; j<n-1; j++)
        {
            if (wordlens[j]>wordlens[j+1])
            {
                tmp = wordlens[j];
                for (int k = 0; k<wordlens[j];k++)
                {
                    word[k] = words[j][k];
                }
                wordlens[j] = wordlens[j+1];
                for (int k = 0; k<tmp;k++)
                {
                    if (k > wordlens[j]-1) 
                    {
                        words[j][k] = 0;
                    }
                    words[j][k] = words[j+1][k];
                }
                wordlens[j+1] = tmp;
                for (int k = 0; k<tmp;k++)
                {
                    words[j+1][k] = word[k];
                }
                for (int k = 0; k<wordlens[j+1];k++)
                {
                    word[k] = 0;
                }
            }
        }
    }
    for (int i =0; i<n;i++)
    {
        for (int j = 0; j<n-1; j++)
        {
            if (wordlens[j] == wordlens[j+1])
            {
                if (strcmp(words[j],words[j+1]) == 1)
                {
                    for (int k = 0; k<wordlens[j];k++)
                    {
                        word[k] = words[j][k];
                    }
                    for (int k = 0; k<wordlens[j];k++)
                    {
                        words[j][k] = words[j+1][k];
                    }
                    for (int k = 0; k<wordlens[j];k++)
                    {
                        words[j+1][k] = word[k];
                    }
                    for (int k = 0; k<wordlens[j];k++)
                    {
                        word[k] = 0;
                    }
                }
            }
        }   
    }
    for (int i = 0; i < n; i++)
    {
        if (i > 0 && strcmp(words[i],words[i-1]) == 0) continue;
        for (int j = 0; j<wordlens[i]; j++)
        {
            printf("%c",words[i][j]);
        }
        printf("\n");
    }
}