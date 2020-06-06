#include <stdio.h>
int main(void){
    int testcase,h,m;
    float answer;
    scanf("%d",&testcase);
    while(testcase--){
        scanf("%d:%d",&h,&m);
        if(h*60+m<60){
        printf("%.1lf %.1lf\n",(h*60+m)*0.5,(h*60+m)*6.0);   
        }
        if(h*60+m>=60){
        printf("%.1lf %.1lf\n",(h*60+m)*0.5,((h*60+m)%60)*6.0);   
        }
    }

}