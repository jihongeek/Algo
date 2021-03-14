#include <stdio.h>
int main(void){
	int a, b, n, x, y, lcm,gcd,t;
    scanf("%d",&t);
    while (t--)
    {
	    scanf("%d %d",&x,&y);
	    a = x;
	    b = y;
	    while (y != 0)
	    {
	    	n = x % y;
	    	x = y;
	    	y = n;
	    }
	    lcm = x * (a / x) * (b / x);
	    printf("%d\n",lcm);
    }

}
