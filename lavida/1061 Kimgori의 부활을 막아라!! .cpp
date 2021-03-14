#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAX_I 20
int main(void){
    int testcase,n,m,tmp;
    int E[MAX_I];
    scanf("%d",&testcase);
    while (testcase--)
    {
        scanf("%d %d",&n,&m);
        for (int i = 0; i<n; i++)
        {
            scanf("%d",&E[i]);
        }
        sort(E,E+n);
        printf("%d\n",E[m-1]);
    }
    
}