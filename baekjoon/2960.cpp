#include <stdio.h>
#include <vector>
#include <cmath>
using namespace std;
int main(void){
    vector <int> numbers;
    int k,n,count,d,num;
    scanf("%d %d",&n,&k);
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
                if (count == k-1)
                {
                    num = numbers[i+(j)*numbers[i]];
                }
                numbers[i+(j)*numbers[i]] =0 ;
                count++;
            }
        }
    }
    printf("%d\n",num);
}