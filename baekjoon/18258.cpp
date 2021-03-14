#include <stdio.h>

int queue[2000000];

int main(void)
{
    char input[6] = {0,};
    int x,m;
    int front = 0;
    int rear = 0;
    int size = 0;
    scanf("%d",&m);
    for (int i = 0; i<m; i++)
    {
        scanf("%s",&input);
        if (input[0] == 112)
        {
            if (input[2] == 112)
            {
                if (size == 0)
                {
                    printf("-1\n");
                }
                else
                {
                    printf("%d\n", queue[front]);
                    queue[front] = 0;
                    if (front == 1999999)
                    {
                        front = 0;
                    }
                    else if (size != 0)
                    {
                        front++;
                    }
                    size--;
                    if (size == 0)
                    {
                        front = 0;
                        rear = 0;
                    }
                }
            }
            else
            {
                if (rear == 1999999)
                {
                    rear = 0;
                }
                else if (size != 0)
                {
                    rear++;
                }
                scanf("%d",&x);
                queue[rear] = x;
                size++;
            }
        }
        else if (input[0] == 115)
        {
            printf("%d\n",size);
        }
        else if (input[0] == 102)
        {
            if (size == 0) printf("-1\n");
            else printf("%d\n",queue[front]);
        }
        else if (input[0] == 98)
        {
            if (size == 0) printf("-1\n");
            else printf("%d\n",queue[rear]);
        }
        else if (input[0] == 101)
        {
            if (size == 0) printf("1\n");
            else printf("0\n");
            
        }
    }
}