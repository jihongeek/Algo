#include <cstdio>
#include <algorithm>

using namespace std;

bool compare(char a, char b)
{
    return a > b;
}

int main(void)
{
    char numberArray[100001] = {'\0',};
    int size = 0;
    scanf("%s",numberArray);
    
    for (int i = 0; numberArray[i] != '\0'; i++)
    {
        size++;   
    }
    
    sort(numberArray,numberArray+size,compare);
    int sum = 0;
    for (int i=0; i < size; i++) 
    {
        sum += (numberArray[i]-'0');
    }
    if (size >= 2 && sum % 3 == 0 && numberArray[size-1] == '0')
    {
        for (int i = 0; i < size; i++)
        {
            printf("%c",numberArray[i]);
        }
        printf("\n");
    }
    else
    {
        printf("-1\n");
    }


    return 0;
}


