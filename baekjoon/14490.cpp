#include <stdio.h>
int main(void){
	long long a, b, k, n, m,gcd;
	scanf("%lld:%lld",&n,&m);
	a = n;
	b = m;
	while (m != 0)
	{
		k = n % m;
		n = m;
		m = k;
	}
    gcd = n;
	
	printf("%lld : %lld",a/gcd,b/gcd);

}