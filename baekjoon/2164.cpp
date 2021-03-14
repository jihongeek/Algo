#include <stdio.h>

int queue[500000];

int main(void)
{
    int n,x;
    int front = 0;
    int rear = -1;
    int size = 0;
    scanf("%d",&n);
    for (int i = 0; i < n; i++)
    {
        queue[i] = i+1;
        rear++;
        size++;
    }

    for (int i = 0; i<n; i++)
    {
        if (n == 1) break;
        queue[front] = 0;
        if (front == 499999)
        {
            front = 0;
        }
        else if (size != 0)
        {
            front++;
        }
        size--;
        
        if (size == 1)
        {
            break;
        }

        x = queue[front];
        queue[front] = 0;
        if (front == 499999)
        {
            front = 0;
        }
        else if (size != 0)
        {
            front++;
        }
        size--;

        if (rear == 499999)
        {
            rear = 0;
        }
        else if (size != 0)
        {
            rear++;
        }
        queue[rear] = x;
        size++;
    }
    printf("%d",queue[front]);
}