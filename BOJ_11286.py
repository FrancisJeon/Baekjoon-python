# 절댓값 힙 210926
""" 
배열에 정수를 넣는데 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거한다.
만약 절댓값이 가장 작은 값이 여러개일 때는 가장 작은수를 출력하고 그 값을 배열에서 제거한다
0이 들어가면 가장 작은 값을 제거하고 출력해야 한다.

일단 모든 값을 abs() 처리를 해주는데 push의 경우 abs 처리 안된 리스트를 따로 하나 관리하기..

정답 코드를 살펴보니 (입력값i, 절대값(i))로 이뤄진 인풋값을 넣어주더라
"""
# 1차 -> 시간 초과, stdout.write를 써도 시간초과가 뜬다
""" import sys
import heapq
input = sys.stdin.readline

all_inputs = [] # 모든 값을 담아두는 리스트
h = [] # 절대값이 담기는 힙

for _ in range(int(input())):
    x = int(input()); abs_x = abs(x)
    if x: 
        all_inputs.append(x)
        heapq.heappush(h, abs_x)
    elif x == 0:
        if not h: print(0)
        elif h:
            val = heapq.heappop(h)
            idx = all_inputs.find(val)
            if all_inputs:
                
                print(-val)
            else:
                del all_inputs[idx]
                print(val) """

# 2차 -> (abs_x, x) 를 넣은 경우엔 양 쪽 다 최소값을 먼저 넣는 힙이 만들어진다.
'''
import sys
import heapq
input = sys.stdin.readline

h = []

for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(h, (abs(x), x)) # 절대값, 원래값 담아서 넣어주면 절대값 순서대로 쌓인다. x[0] x[1] 자동 정렬이 되는지 확인해보자
    elif x == 0:
        # print(h) # 얘가 출력초과 원인
        if not h: print(0)
        elif h:
            val = heapq.heappop(h)
            ans = val[1]
            print(ans)
'''
# 숏코딩
import sys
import heapq
input = sys.stdin.readline

h = []
for _ in range(int(input())):
    x = int(input())
    if x == 0: print(heapq.heappop(h)[1] if h else 0)
    else: heapq.heappush(h, (abs(x), x))
        