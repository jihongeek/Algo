#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int r,c;
    string puzzle[20] = {};
    vector <string> words;
    cin >> r >> c;
    
    for (int i = 0; i < r; i++)
    {
        cin >> puzzle[i];
    }
    for (int row = 0; row < r; row++)
    {
        string tempString = "";
        for (int col = 0; col < c; col++)
        {
            if (puzzle[row][col] == '#')
            {
                if (tempString.length() > 1)
                {
                    words.push_back(tempString);
                }
                tempString = "";
            }
            else
            {
                tempString += puzzle[row][col]; 
            }
        }
        if (tempString.length() > 1) 
            words.push_back(tempString);
        tempString = "";
    }

    for (int col = 0; col < c; col++)
    {
        string tempString = "";
        for (int row = 0; row < r; row++)
        {
            if (puzzle[row][col] == '#')
            {
                if (tempString.length() > 1)
                {
                    words.push_back(tempString);
                }
                tempString = "";
            }
            else
            {
                tempString += puzzle[row][col]; 
            }
        }
        if (tempString.length() > 1)
            words.push_back(tempString);
        tempString = "";
    }
    sort(words.begin(),words.end());
    if (words.size() > 0)
        cout << words[0];
}