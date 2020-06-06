#include <stdio.h>
#include <math.h>
int main(void){
    int T,N1,N2,N3,M1,M2,M3,A;
    scanf("%d",&T);
    while (T--){
    scanf("%d %d %d",&N1,&N2,&N3);
    scanf("%d %d %d",&M1,&M2,&M3);
    A = 0;
    if (abs(N1 - M1)>5){
        A =  A + 10 - abs(N1 - M1);    
    }   else
    {
        A = A + abs (N1 - M1);
    }
    if (abs(N2 - M2)>5){
        A = A + 10 - abs(N2 - M2);    
    }   else
    {
        A = A + abs (N2 - M2);
    }
    if (abs(N3 - M3)>5){
        A = A + 10 - abs(N3 - M3);    
    }   else
    {
        A = A + abs (N3 - M3);
    }
    printf("%d\n",A);
    }
}