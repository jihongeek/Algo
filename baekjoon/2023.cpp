#include <iostream>
#include <cmath>
using namespace std;

/*
    n에 대해서 n보다 작은 소수로 나누어 떨어지지 않으면 n은 소수다.
    또한 n에 대해서 sqrt(n) 보다 작은 수로 나누었을 때 나누어 떨어지지 않으면 소수다.
    위를 통해서 sqrt(10^8) 까지의 소수와 소수 표를 이용해서 소수 판별을 할 수 있다.
    또한 특정 자리수로 만들어지는  소수가 아니면 신기한 소수가 될 수 없으므로 이를 이용해 풀면 된다.
*/
int primes[10000]; 
int prime_table[10000];
int prime_count;

bool isPrime(int num)
{
    if (num == 1) return false;
    if (num < 10000)
    {
        if (prime_table[num]) return true;
    }
    for (int i = 0; i < prime_count; i++)
    {
        if (primes[i] >= num) return true;
        if (num % primes[i] == 0) return false;   
    }
    return true;
}

int mypow(int a,int n)
{   
    int result = a;
    if (n == 0) return 1;
    for (int i = 1; i < n; i++)
    {
        result *= a;
    }      
    return result;
}

bool check(int n, int digit)
{
    int digitNumber; 
    while (digit > -1)
    {
        digitNumber =  n / mypow(10,digit);
        if (isPrime(digitNumber)) 
            digit--;
        else
            return false;
    }
    return true;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,start,end;
    cin >> n;
    start = mypow(10,n-1);
    end = 0;
    for (int i = 0; i < n; i++)
    {
        end += (9*mypow(10,i));
    }

    for (int i = 2; i < 10000; i++)
    {
        bool iIsPrime = true;
        for (int j = 2; j < 100; j++)
        {
            if (i <= j) break;  
            if (i % j == 0)
            {
                iIsPrime = false;
                break;
            }             
        }
        if (iIsPrime)
        {
            primes[prime_count++] = i;
            prime_table[i] = 1;
        }
    }
    
    
    for (int i = start; i <= end; i++)
    {
        if(check(i,n-1)) cout << i << '\n'; 
    }
}