#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
    int inputnum,sum;
    vector <int> odd_nums;
    sum = 0;
    for (int i = 0;i<7;i++)
    {
        scanf("%d",&inputnum);
        if (inputnum % 2 != 0)
        {
            odd_nums.push_back(inputnum);
        }
    }
    if (odd_nums.size()==0)
    {
        printf("%d\n",-1);
    }
    else
    {
        for (int i = 0; i<odd_nums.size();i++)
        {
            sum = sum + odd_nums[i];
        }
        printf("%d\n",sum);
        sort(begin(odd_nums),end(odd_nums)); 
        printf("%d\n",odd_nums[0]);
    }
    
}