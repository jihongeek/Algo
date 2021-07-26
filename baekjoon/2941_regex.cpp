# include <iostream>
# include <cstdio>
# include <regex>
# include <string>
using namespace std;

int main(void)
{
    char buff[101];
    scanf("%s",buff);
    string word = buff;
    regex rx("c=|c-|dz=|d-|lj|nj|s=|z=");
    word = regex_replace(word,rx," ");
    printf("%d",word.length());
}
