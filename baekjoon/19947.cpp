#include <stdio.h>

int main(void)
{
    int h,y;
    int ans;
    double invest[] = {0, 0.05, 0 , 0.2, 0, 0.35};
    ans = 0;
    scanf("%d %d",&h,&y);
    ans = h;
    if (y && y<=5)
    {
        if (y%2)
        {
            ans =  (int)(ans * (1.0 + invest[y]));
        }
        else if (y == 2)
        {
            ans =  (int)(ans * (1.0 + invest[1]));
            ans =  (int)(ans * (1.0 + invest[1]));
        }
        else if (y == 4)
        {
            ans =  (int)(ans * (1.0 + invest[1]));
            ans =  (int)(ans * (1.0 + invest[3]));
        }
    } 
    else if (y>5)
    {
        if (y == 6)
        {
            ans =  (int)(ans * (1.0 + invest[3]));
            ans =  (int)(ans * (1.0 + invest[3]));
        }
        else if (y == 7)
        {
            ans =  (int)(ans * (1.0 + invest[3]));
            ans =  (int)(ans * (1.0 + invest[3]));
            ans =  (int)(ans * (1.0 + invest[1]));
        }
        else if (y == 8)
        {
            ans =  (int)(ans * (1.0 + invest[5]));
            ans =  (int)(ans * (1.0 + invest[3]));
        }
        else if (y == 9)
        {
            ans =  (int)(ans * (1.0 + invest[3]));
            ans =  (int)(ans * (1.0 + invest[3]));
            ans =  (int)(ans * (1.0 + invest[3]));
        }
        else if (y == 10)
        {
            ans =  (int)(ans * (1.0 + invest[5]));
            ans =  (int)(ans * (1.0 + invest[5]));
        }
    }
    printf("%d",ans);
}