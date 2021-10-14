# 단지번호붙이기 211014
""" 
0이 아닌곳들중에 동서남북이 한곳이라도 이어진 집들은 이어서 같은 단지에 속한다고 한다. 
* 출력
그래프가 주어지면 몇개의 단지가 존재하는지 출력하라 + 단지에 속하는 집의 수를 오름차순으로 정렬해서 한줄에 하나씩 출력

* 알고리즘
BFS와 DFS중 전체 연결만 확인하기 좋은 방법은 DFS가 아닐까? 깊이 우선으로 전부를 다 들렀다 오니까.. 사실 차이가 있을까 싶다만 DFS를 활용해서 모든 곳에 들러서 개수를 담고 들린곳은 전부 이미 들른곳이라는 표시를 해주자.
검색조건 -> 오른쪽 또는 아래 (좌->우, 상->하로 서칭하기 때문에 최초 지점에서 우측과 하단으로 처음에 뻗어나가야 한다.)
"""
# 내 풀이
import sys
import heapq
input = sys.stdin.readline
n = int(input())
MAP = [input().rstrip() for _ in range(n)]
ans = 0
ans_arr = []

for i in range(n):
    for j in range(n): # n * n 형태여서 가능함
        if MAP[i][j] == 1: 
            heapq.heappush(ans_arr, dfs(i,j))
            ans += 1

print(ans)
print(*ans_arr)

def dfs(i, j): # i와 j의 좌표를 가지고 dfs 진행하기
    # 1을 만나면 바로 DFS 또는 BFS를 진행해준다. 1은 9로 바꾸고 바꿀 때마다 개수를 측정해준다.
    # 반복문을 다 돌고 나오면 ans 개수는 하나 증가시켜주고 계산한 개수는 heap에 넣어준다. heappush
    # 함수의 리턴값은 9로 변화시킨 집의 개수
    num = 0
    # 사방이 1인지 확인하는 방법을 반복해서 큐또는 스택에 담아주기
    pass
    
