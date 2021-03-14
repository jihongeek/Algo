#include <stdio.h>
#include <string>
using namespace std;
int main(void){
    char cr_alphabets[8][4] = {"c=","c-","dz=","d-","lj","nj","s=","z="};
    char inputchar[100];
    int where_cr,i;
    string inputstr,cr;
    scanf("%s",&inputchar);
    inputstr = inputchar;
    i = 0;
    while(1)
    {
        if (i == 8)
        {
            break;
        }
        cr = cr_alphabets[i];
        where_cr = inputstr.find(cr_alphabets[i]);     
        if(where_cr == string::npos)
        {
            i = i + 1;
            continue;
        }
        inputstr.replace(where_cr,cr.length()," ");
    }
    printf("%d\n",inputstr.length());

}