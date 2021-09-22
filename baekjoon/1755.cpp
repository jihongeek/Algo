#include <iostream>
#include <string>

using namespace std;

struct numberStruct
{
    int num;
    string firstDigit;
    string secondDigit;
};

int main(void) 
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    int m,n;
    numberStruct numbers[100] = {};
    string digitStrings[10] = {"zero","one","two","three","four","five","six","seven","eight","nine"}; 
    
    cin >> m >> n;

    for (int i = m; i <= n; i++)
    {
        numbers[i-m].num = i;
        if (numbers[i-m].num / 10 == 0)
            numbers[i-m].firstDigit = digitStrings[i%10];
        else 
        {
            numbers[i-m].firstDigit = digitStrings[i/10];
            numbers[i-m].secondDigit = digitStrings[i%10];
        }
    }

    for (int i = 0; i < n-m+1; i++)
    {
        for (int j = 0; j < n-m; j++)
        {
            numberStruct temp;
            if (numbers[j].firstDigit > numbers[j+1].firstDigit)
            {
                temp = numbers[j];
                numbers[j] = numbers[j+1];
                numbers[j+1] = temp;
            }
            if (numbers[j].firstDigit == numbers[j+1].firstDigit)
            {
                if (numbers[j].secondDigit > numbers[j+1].secondDigit)
                {
                    temp = numbers[j];
                    numbers[j] = numbers[j+1];
                    numbers[j+1] = temp;
                }
            }
        }
    }
    bool isEnd = false;
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (numbers[i*10+j].num == 0)
            {
                isEnd = true;
                break;
            }
            cout << numbers[i*10+j].num << " ";
        }
        if (isEnd) break;
        cout << "\n";
    }
    
}