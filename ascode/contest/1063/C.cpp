#include <stdio.h>
#include <math.h>
int t;
int cases[28];
double units[7] = {0.393,1.000,0.001,1.609,0.002,0.109,1.852};
int main(int argc, char const *argv[])
{

    scanf("%d",&t);
    int k = 0;
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 0; j < 7; j++)
        {
            cases[k] = (int)(i * units[j]*1000)/1 +  (int)((5-i)*units[0]*1000)/1;
            k++;
        }
    }
    for (int nowT = 0; nowT < t; nowT++) {
        double d;
        scanf("%lf",&d);
        bool isDuck = false;
        for (int i = 0; i < 28; i++) {
            if (cases[i] == (int)((d*1000)/1)) {
                isDuck = true;
                break;
            }
        }
        if (isDuck) {
            printf("duck\n");
        }
        else {
            printf("goose\n");
        }
    }
    return 0;
}

