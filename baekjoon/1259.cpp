#include <cstdio>
using namespace std;

int main(void)
{
    while (true)
    {
        int length = 0;
        bool isPalindrome = true;
        char number[6];
        scanf("%s",number);

        if (number[0] == '0' and number[1] == 0)
            break;
     
        while (number[length] != 0)
        {
            length++;
        }

        for (int i = 0; i < length; i++)
        {
            if (number[i] != number[length - i - 1])
            {
                isPalindrome = false;
                break;
            }
        }

        if (isPalindrome)
        {
            printf("yes\n");
        }
        else
        {
            printf("no\n");
        }
    }
}