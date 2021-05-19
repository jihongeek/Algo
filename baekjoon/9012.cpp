#include <iostream>
using namespace std;

class node {
    public:
        node(int data_, node * next_=0)
        {
            data = data_;
            next = next_;
        }
        int data;
        node * next;
};

class stack {
    public:
        stack()
        {
            top = 0;
        }
        bool isEmpty() 
        {
            if (top == 0) return true;
            return false;
        }
        void Insert(int data)
        {
            if (top == 0) 
            {
                top = new node(data);
                return;
            }
            top = new node(data,top);
        }
        int Pop()
        {
            if (isEmpty()) return -1; 
            node * ToPop;
            int el;
            ToPop = top;
            el = ToPop -> data;
            top = top->next;
            delete ToPop;
            return el;
        }
        node * top;
};

int main(void)
{
    char ps[51];
    int testcase;
    scanf("%d",&testcase);
    while(testcase--)
    {
        int isVps = 0;
        stack stack1;
        scanf("%s",ps);
        for (int i = 0; ps[i] != 0; i++)
        {
            if (ps[i] == '(') 
            {
                stack1.Insert((int) ps[i]);
            }
            else
            {
                if (stack1.Pop() == '(')
                {
                    isVps = 1;
                }
                else
                {
                    isVps = 0;
                    break;
                }
            }
        }
        if (!stack1.isEmpty()) isVps = 0;
        if (isVps)
        {
            printf("YES\n");   
        }
        else
        {
            printf("NO\n");
        }
    }

}