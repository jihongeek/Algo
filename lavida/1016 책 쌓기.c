#include <stdio.h>
int main(void){
    int testcase,cycle,m_num;
    float L,N;
    scanf("%d",&testcase);
    while (testcase--)
    {
        L = 0;
        m_num = 2;
        cycle = 0;
        scanf("%f",&N);
        while (N > L)
        {
            L = L + 1/(float)m_num;
            cycle = cycle + 1;
            m_num = m_num + 1;
        }
        printf("%d\n",cycle);
    }
    
}