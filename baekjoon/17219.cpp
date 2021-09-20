#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main(void)
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    int n,m;
    unordered_map <string,string> map;

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        string address, password;
        cin >> address >> password;
        if (map.find(address) == map.end())
        {
            map.insert({address,password});
        }
    }

    for (int i = 0; i < m; i++)
    {
        string address ="";
        cin >> address;
        cout << map[address] << "\n";
    }

}