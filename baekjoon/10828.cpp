#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int n; // 명령의 갯수
    stack <int> my_stack; // 정수를 저장하는 스택

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string command;
        int number;

        cin >> command;
        if (command == "push")
        {
            cin >> number;
            my_stack.push(number);
        }
        if (command == "pop")
        {
            if (my_stack.size() == 0)
            {
                cout << -1 << "\n";
                continue;
            }
            cout << my_stack.top() << "\n"; 
            my_stack.pop();
        }
        if (command == "size")
        {
            cout << my_stack.size() << "\n";
        }
        if (command == "empty")
        {
            cout << my_stack.empty() << "\n";
        }
        if (command == "top")
        {
            if (my_stack.size() == 0)
            {
                cout << -1 << "\n";
                continue;
            }
            cout << my_stack.top() << "\n";
        }
    } 
}