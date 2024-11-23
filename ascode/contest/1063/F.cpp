#include <stdio.h>
#include <math.h>


int main(int argc, char const *argv[])
{
    double a,b,c;
    scanf("%lf %lf %lf",&a,&b,&c);
    double x = (-b/ (2*a)) + 0.00005;
    printf("%.4lf\n",x); 
    return 0;
}
