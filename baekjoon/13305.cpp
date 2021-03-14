#include <stdio.h>

int gas[100000];
int distance[99999];
long long money = 0;
int lastGas = 1000000000;

int main(void)
{
    int n;
    scanf("%d",&n);
    
    for (int i = 0; i< n-1; i++)
    {
        scanf("%d",&distance[i]);
    }
    for (int i = 0; i< n; i++)
    {
        scanf("%d",&gas[i]);
    }
    
    // 주유소의 기름 가격을 보고 가격이 최대한 낮을 때 최대한 많은 거리를 이동해야 한다.
    for (int i = 0; i< n; i++)
    {   
        // 이전 주유소 가격보다 현재 주유소의 기름 값이 저렴할때
        if (gas[i] < lastGas)
        {
            // 현재 주유소의  기름 값으로 이동하기
            money = money + gas[i] * (long long)distance[i];
            // 이전 주유소의 기름 값을 현재 주유소로 바꾸기
            lastGas = gas[i];
        }
        // 비싸거나 같을때 
        else
        {
            // 이전 주유소의 기름 값으로 이동하기
            money = money + lastGas * (long long)distance[i];
        }
    }
    printf("%lld",money);
    


}