#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;
int main(void){
    vector <int> numbers;
    int m,n,count,d,num;
    scanf("%d %d %d",&m,&n,&d);
    count = 0 ;
    for (int i = 2;i<n+1;i++)
    {
        numbers.push_back(i);
    }
    for (int i = 0;numbers[i]<sqrt(n);i++)
    {
        if (numbers[i] == 0)
        {
            continue;
        }
        for (int j = 1;j<n/numbers[i]+1;j++)
        {
            if(numbers[i+(j)*numbers[i]] == 0)
            {
                continue;
            }
            else
            {
                numbers[i+(j)*numbers[i]] =0 ;
            }
        }
    }
    for (int i = 0;i<n-1;i++)
    {
        if(numbers[i]!=0)
        {
            num = numbers[i];
            for (int j = 0;num!=0;j++)
            {
                if (num % 10 == d)
                {
                    count++;
                    break;
                }
                num = num / 10;
            }
        }
    }
    printf("%d\n",count);
}