#include <stdio.h>
#include <algorithm>

using namespace std;

int numbers[51];

bool desc(int a, int b)
{ 
    return a > b; 
}

int main(void)
{
    
    int num;
    long long answer;
    

    scanf("%d",&num);
    for (int i = 0; i<num; i++)
    {
        scanf("%d",&numbers[i]);
    }
    sort(numbers,numbers+51,desc);
    answer = numbers[0]*numbers[num-1];
    printf("%lld\n",answer);
}