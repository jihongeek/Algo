#include <cstdio>
using namespace std;

int main()
{
    int first[10002] = {0,} ,second[10002] = {0, };
    int answer[10002] = {0,};
    
    char temp1[10002] = {'X',}, temp2[10002] = {'X',}; 
    scanf("%s %s",temp1,temp2);

    int zeroLength = 0;
    for (int i = 0; i < 10002; i++)
    {   
        if (temp1[i] == NULL)
            zeroLength++;
    }
    for (int i = 0; i+zeroLength <10002; i++)
    {
        first[zeroLength + i] = temp1[i] - '0';
    }
    zeroLength = 0;
    for (int i = 0; i < 10002; i++)
    {   
        if (temp2[i] == NULL)
            zeroLength++;
    }
    for (int i = 0; i+zeroLength <10002; i++)
    {
        second[zeroLength + i] = temp2[i]-'0';
    }
    
    int carry = 0;
    for (int i = 10001; i > -1; i--)
    { 
        int sum = first[i] + second[i] + carry;
        if (carry > 0)
            carry--; 
        carry += (sum / 10);
        answer[i] = sum % 10;
    }
    bool isStarted = false;
    for (int i = 0; i < 10002; i++)
    {
        if (!isStarted && answer[i] != 0) isStarted = true;
        if (isStarted) printf("%d",answer[i]);
    }
}