#include <stdio.h>
#include <stdlib.h> 
#include <time.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int num;
	int lotto_nums[6] = {0,};
	int i,j,now,tmp,lotto_num,isSame;
	
	srand(time(NULL)); // rand함수 시드값 설정
	
	printf("로또게임을 몇번 수행할까요? ");
	scanf("%d",&num);
	
	for (now = 1; now < num+1; now++)
	{
		printf("[%2d] ",now);
		for (i = 0; i<6 ; i++)
		{
			while (1)
			{
				isSame = 0;
				lotto_num = (rand() % 6) + 1;
				for (j = 0; j<i; j++)
				{
					if (lotto_nums[j] == lotto_num)
					{
						isSame = 1;
						break;
					}
				}
				if (isSame == 0)
				{
					break;
				}
			}
			lotto_nums[i] = lotto_num;	
		}
		
		
		for (i = 0; i<6 ; i++)
		{	
			for (j = 0; j < 5; j++)
            {
                if (lotto_nums[j] > lotto_nums[j + 1])
                {
                    tmp = lotto_nums[j];
                    lotto_nums[j] = lotto_nums[j + 1];
                    lotto_nums[j + 1] = tmp;
                }
            }	
		}
		
		
		for (i = 0; i<6 ; i++)
		{	
			printf("%d ",lotto_nums[i]);	
		}
		printf("\n");	
	}
	return 0;
}