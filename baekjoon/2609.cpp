#include <stdio.h>
int main(void){
	long long a, b, n, x, y, lcm,gcd;
	scanf("%lld %lld",&x,&y);
	a = x;
	b = y;
	while (y != 0)
	{
		n = x % y;
		x = y;
		y = n;
	}
    gcd = x;
	lcm = x * (a / x) * (b / x);
	printf("%lld\n",gcd);
	printf("%lld\n",lcm);

}