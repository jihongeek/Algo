#include <stdio.h>

int main(void) 
{
   char word[1001];
   scanf("%s",word);
   for (int i = 0; word[i] != NULL; i++)
   {
       printf("%c",((word[i]-'A'+26)-3)%26+'A');
   } 
}