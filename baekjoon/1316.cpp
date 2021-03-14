#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
int main(void){
    int N,k,count,isgroup;
    char words[100][100];
    char cutalphabet;
    vector <int> cutalphabets;
    string wordstr;
    scanf("%d",&N);
    count = 0;
    isgroup = 2;
    for (int i = 0;i<N;i++)
    {
        scanf("%s",words[i]);
    }
    for (int i = 0;i<N;i++)
    {    
        cutalphabets.clear();
        wordstr = words[i];
        for (int j = 0; j<wordstr.length(); j++)
        {
            k = j + 1;
            if(wordstr[j] != wordstr[k])
            {
                cutalphabets.push_back(wordstr[j]);
            }
        }
        if (cutalphabets.size() == 1)
        {
            count = count + 1;
            continue;
        }
        for (int j = 0; j<cutalphabets.size(); j++)
        {
            for (int k = j + 1; k<cutalphabets.size(); k++)
            {
                if(cutalphabets[j] == cutalphabets[k])
                {
                    isgroup = 0;
                    break;
                }
                else
                {
                    isgroup = 1;
                }
                
            }
            if (isgroup == 0)
            {
                break;
            }
        }
        if (isgroup == 1)
        {
            count = count + 1;
        }
    }
    printf("%d",count);
}

