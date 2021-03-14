#include <stdio.h>
#include <cmath>
#include <vector>
using namespace std;
int main(void){
    vector <int> numbers;
    int n,count;
    numbers.reserve(123456);
    while (1)
    {
        count = 0;
        scanf("%d",&n);
        if (n == 0)
        {
            break;
        }
        for (int i = 2;i<=2*n+1;i++)
        {
            numbers.push_back(i);
        }
        for (int i = 0;numbers[i]<sqrt(2*n)+1;i++)
        {
            if (numbers[i] == 0)
            {
                continue;
            }
            for (int j = 1;j<2*n/numbers[i]+1;j++)
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
        for (int i = 0;i<2*n-1;i++)
        {
            if(numbers[i]!=0 && numbers[i]>n&& numbers[i]<=2*n)
            {
                count +=1;
            }
        }
        printf("%d\n",count);
        numbers.clear();
    }
}       