#include <stdio.h>
int main(void){
    int n,s[10000],c[10000],l[10000],max,first,c_min,l_min;
    max = 0;
    scanf("%d",&n);
    for (int i = 0;i<n;i++)
    {
        scanf("%d %d %d",&s[i],&c[i],&l[i]);
    }
    for (int i = 0;i<n;i++)
    {
        if (n==1)
        {
            first = 1;
            break;
        }
        else
        {
            if (s[i] > max)
            {
                max = s[i];
                c_min = c[i];
                l_min = l[i];
                first  = i+1;
            }
            else if (s[i] == max)
            {
                if (c[i] < c_min)
                {
                    c_min = c[i];
                    first = i+1;
                }
                else if (c[i] == c_min)
                {
                    if (l[i] < l_min)
                    {
                        l_min = l[i];
                        first = i+1;
                    }
                }
            }
        }
        
    }
    printf("%d\n",first);                        
}