#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int main(void){
    vector <int> v;
    int n,m,p;
    scanf("%d %d",&n,&m);
    for (int i =2; i<m+1;i++)
    {
        v.push_back(i);
    }
    for (int i =0; i<v.size();i++)
    {
        p = v[i];
        if (i > 1)
        {
            if (p%i==0)
            {
                v.erase(v.begin()+i);
            }
        }
    }
    for (int i =0; i<v.size();i++)
    {
        if (v[i]>=n)
        {
            printf("%d\n",v[i]);
        }
    }
}