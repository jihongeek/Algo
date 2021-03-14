#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Student{
public:
    string name;
    int kor;
    int eng;
    int math;
    Student(string name, int kor, int eng, int math):name(name),kor(kor),eng(eng),math(math){}
    
};
bool compare(Student a, Student b){
    if(a.kor == b.kor){
        if (a.eng == b.eng)
        {
            if (a.math == b.math)
            {
                return a.name < b.name;
            }
            else
            {
                return a.math > b.math;
            }
            
        }
        else 
            return a.eng < b.eng;
    }else{               
        return a.kor > b.kor;
    }
}

int main(void)
{
    vector<Student> v;
    int n;
    char name[11];
    int kor,eng,math; 
    scanf("%d",&n);
    for (int i = 0; i< n; i++)
    {
        scanf("%s",name);
        scanf("%d %d %d",&kor,&eng,&math);
        v.push_back(Student(name,kor,eng,math));
    }
    sort(v.begin(),v.end(),compare);
    for (int i = 0; i<n; i++)
    {
        cout << v[i].name ;
        cout << '\n';
    }
}