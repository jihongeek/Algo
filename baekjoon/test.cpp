#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void reverse(char *string)
{
	int i;
	int tmp;
	int len = strlen(string);
	for (i = 0; i < (len-1)/2; i++)
	{
		tmp = string[i];
		string[i] = string[(len-1)-i];
		string[(len-1)-i] = tmp;
	}
}

int main(int argc, char *argv[]) {
	char string[100];
	gets(string);
	puts(string);
	reverse(string);
	puts(string);	
	return 0;
}
