#include <iostream>
#include <stack>

using namespace std;

int main(void)
{
    int n;
    stack <int> seriesStack,seriesTempStack;
    stack <char> cmdTempStack, cmdStack;
    
    cin >> n;
    
    for (int i = 0; i < n; i++)
    {
        int number;
        cin >> number;
        seriesTempStack.push(number);
    }
    
    for (int i = 0; i < n; i++)
    {
        seriesStack.push(seriesTempStack.top());
        seriesTempStack.pop();
    }

    for (int i = 1; ;)
    {
        if (!seriesTempStack.empty() && seriesTempStack.top() == seriesStack.top())
        {
            seriesStack.pop();
            seriesTempStack.pop();
            cmdTempStack.push('-');
        }
        else 
        {
            if (i > n) break;
            cmdTempStack.push('+');
            seriesTempStack.push(i);
            i++;
        }
    }

    while (!cmdTempStack.empty())
    {
        cmdStack.push(cmdTempStack.top());
        cmdTempStack.pop();
    }

    if (seriesStack.empty())
    {
        while (!cmdStack.empty())
        {
            cout << cmdStack.top() << '\n';
            cmdStack.pop();
        }
    }
    else
    {
        cout << "NO\n";
    }

}