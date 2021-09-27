#include <iostream>
#include <queue>

using namespace std;

int main(void)
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    priority_queue <int> heap;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        if (num == 0)
        {
            if (heap.empty()) 
                cout << 0 <<'\n';
            else
            {
                cout << -heap.top() << '\n';
                heap.pop();
            }
        }
        else 
            heap.push(-num);    
    }
}