#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char zeroOnes[1000001];
int a[1000000];

int main(void)
{
    int testcase,i,j;
    int length;
    scanf("%s",zeroOnes);
    length = strlen(zeroOnes);
    a[0] = 0;
    for (int i = 0; i < length - 1; i++)
    {
        if (zeroOnes[i] == zeroOnes[i+1])
        {
            a[i+1] = a[i];
        }
        else
        {
            a[i+1] = a[i] + 1;
        }
    }
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d",&i,&j);
        if (a[i] == a[j])
        {
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
        }
        
    }
    
}