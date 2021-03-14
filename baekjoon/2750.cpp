#include <stdio.h>
#define MAX_I 1001
int main(void){
    int n,temp;
    int v[MAX_I];
    scanf("%d",&n);
    for (int i = 0; i<n;i++)
    {
        scanf("%d",&v[i]);
    }
   	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n - 1; j++)
		{
			if (v[j] > v[j + 1])
			{
				temp = 0;
				temp = v[j+1];
				v[j+1] = v[j];
				v[j] = temp;
			}
		}
    }
    for (int i = 0;i<n;i++)
    {
        printf("%d\n",v[i]);
    }
}