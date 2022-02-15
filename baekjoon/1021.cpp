#include <iostream>
#include <deque>
using namespace std;

/*
    연산 1. : 1,2,3 => 2,3 -> deque의 pop_front
    연산 2. : 1,2,3 => 2,3,1 -> deque의 front -> push_back -> pop_front
    연산 3. : 1,2,3 => 3,1,2 -> deque의 back -> push_front -> pop_back
    
    전략 : 
        왼쪽으로 이동하는 연산의 횟수를 직접 구하고,
        이를 이용해서 오른쪽 연산의 횟수를 구한 다음 더 적은 연산을 진행한다. 
        * size - 왼쪽 이동횟수 = 오른쪽 이동횟수
*/

int main()
{
    // 빠른 입출력을 위한 코드
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    int n,m,size,operation_count;
    deque <int> deq;
    cin >> n >> m;
    size = n;
    operation_count = 0;

    // 1~n deque에 삽입
    for (int i = 1; i <= n; i++)
    {
        deq.push_back(i);
    }

    while (m--)
    {
        int to_pop;
        cin >> to_pop;

        // 왼쪽으로 이동했을 때(2번 연산)의 횟수 구하기
        int left_count = 0;        
        while (deq.front() != to_pop)
        {
            // 왼쪽 이동(2번 연산) 진행
            deq.push_back(deq.front());
            deq.pop_front();
            // 횟수 1 증가
            left_count++;
        }
        // 왼쪽으로 이동한 횟수 만큼 오른쪽 이동 (원상 복구)
        for (int i = 0; i < left_count; i++)
        {
            deq.push_front(deq.back());
            deq.pop_front();
        }

        // 오른쪽으로 이동했을 때의 횟수 구하기
        int right_count = size - left_count;

        // 왼쪽 연산의 횟수가 더 적을 경우 -> 왼쪽 연산 실행
        if (left_count < right_count)
        {
            while (deq.front() != to_pop)
            {
                deq.push_back(deq.front());
                deq.pop_front();
            }
            // 전체 연산 횟수에 왼쪽 연산 횟수 더하기
            operation_count += left_count;
        }
        else // 오른쪽 연산의 횟수가 더 적거나 같을 경우 -> 오른쪽 연산 실행
        {
            while(deq.front() != to_pop)
            {
                deq.push_front(deq.back());
                deq.pop_front();
            }
            // 전체 연산 횟수에 오른쪽 연산 더하기
            operation_count += right_count;
        }
        // 현재 첫번째 원소가 빼낼 원소이므로 1번 연산 진행  
        deq.pop_front();
        // 하나의 원소를 제거했으므로 size 1 빼기
        size--;              
    }
    // 전체 연산 횟수 출력
    cout << operation_count << '\n';
}