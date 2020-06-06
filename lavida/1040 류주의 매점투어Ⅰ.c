#include <stdio.h>
int main(void){
    long long  money,man,ochun,chun,obak,bak,T = 0;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d",&money);
        man = money / 10000;
        money = money - (10000 * man);
        ochun = money / 5000;
        money = money - (5000 * ochun);
        chun = money / 1000;
        money = money - (1000 * chun);
        obak = money / 500;
        money = money - (500 * obak);
        bak = money / 100;
        money = money - (100 * bak);
        printf("%d %d %d %d %d\n",man,ochun,chun,obak,bak);
    }
    
}