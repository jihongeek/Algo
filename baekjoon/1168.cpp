#include <stdio.h>

int queue[100000];
int josephus[100000];
int main(void)
{
    int n,x,k;
    int front = 0;
    int rear = -1;
    int size = 0;
    int index = 0;
    scanf("%d %d",&n,&k);
    for (int i = 0; i < n; i++)
    {
        queue[i] = i+1;
        rear++;
        size++;
    }
    for (int i = 0; i < n; i++)
    {
        if (size == 1)
        {
            josephus[index] = queue[front];
            break;
        }
        for (int j = 0; j < k-1; j++)
        {
            x = queue[front];
            queue[front] = 0;
            if (front == 99999)
            {
                front = 0;
            }
            else if (size != 0)
            {
                front++;
            }
            size--;

            if (rear == 99999)
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
        josephus[index] = queue[front];
        queue[front] = 0;
        if (front == 99999)
        {
            front = 0;
        }
        else if (size != 0)
        {
            front++;
        }
        size--;
        index++;
    }
    for (int i = 0; i < n; i++)
    {
        if (n == 1)
        {
            printf("<%d>",1);
            break;
        }
        if (i == 0)
        {
            printf("<%d, ", josephus[i]);
        }
        else if (i == n - 1)
        {
            printf("%d>", josephus[i]);
        }
        else
        {
            printf("%d, ", josephus[i]);
        }
    }
}