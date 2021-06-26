#include <iostream>
using namespace std;

int main(void)
{
    int n;
    int countMod2,countMod5 = 0;
    cin >> n;
    for (int i = 2; i <= n; i++)
    {
        int numToDivide = i;
        while (numToDivide>0 && (numToDivide % 2 == 0 || numToDivide % 5 == 0))
        {
            if (numToDivide % 2 == 0)
            {
                countMod2+=1;  
                numToDivide =numToDivide/ 2;   
            }
            if (numToDivide == 0) break;
            if (numToDivide % 5 == 0)
            {
                countMod5+=1;    
                numToDivide = numToDivide / 5;   
            }
        }
    }
    cout << ((countMod2 < countMod5) ? countMod2 : countMod5) << "\n";
}