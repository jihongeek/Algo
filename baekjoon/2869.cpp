#include <stdio.h>
int main(void){
    long long a,b,v;
    int day;
    scanf("%lld %lld %lld",&a,&b,&v);
    if ((v-a)/(a-b) == 0)
    {
        day =(v-a)/(a-b); 
    }
    else
    {
        day =(v-a)/(a-b)+1; 
    }
    
    printf("%lld\n",day);
}