#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
    int logNum;
    map <string,bool> mapOfPeople;
    map <string,bool> :: iterator iter;

    scanf("%d",&logNum);

    for (int i = 0; i< logNum; i++)
    {
        char tempName[6], tempBehavior[6];
        string name, behaviour;
        scanf("%s %s",tempName,tempBehavior); 
        name = tempName;
        behaviour = tempBehavior;
        map <string,bool> :: iterator peopleIter =  mapOfPeople.find(name); 
        if (behaviour == "enter")
        {
            if (peopleIter == mapOfPeople.end())
                mapOfPeople.insert(make_pair(name,true));
            else
                peopleIter->second = true;

        }
        else
        {
            mapOfPeople.find(name)->second = false;
        }
        
    }
    for (iter = --mapOfPeople.end(); iter != --mapOfPeople.begin() ; iter--)
    {
            if (iter -> second)
                printf("%s\n",iter->first.c_str());
    }
}