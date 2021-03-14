#include <stdio.h>
int main(void){
    int a;
    scanf("%d",&a);
    for (int i = a/5; i>=0;i--)
    {
        if ((a-5*i)%3 == 0)
        {
            if (a%5 == 0)
            {
                printf("%d\n",a/5);
                break;
            }
            else if (i+(a-5*i)/3 <= a / 3) 
            {
                printf("%d\n",i+(a-5*i)/3);
                break;
            }
            else if (a%3 == 0)
            {
                printf("%d\n",a/3);
                break;
            }
        }
        else if (i == 0)
            {
                printf("-1\n");
            }
        }
}
   