# 단지번호붙이기 211014
""" 
0이 아닌곳들중에 동서남북이 한곳이라도 이어진 집들은 이어서 같은 단지에 속한다고 한다. 
* 출력
그래프가 주어지면 몇개의 단지가 존재하는지 출력하라 + 단지에 속하는 집의 수를 오름차순으로 정렬해서 한줄에 하나씩 출력

* 알고리즘
BFS와 DFS중 전체 연결만 확인하기 좋은 방법은 DFS가 아닐까? 깊이 우선으로 전부를 다 들렀다 오니까.. 사실 차이가 있을까 싶다만 DFS를 활용해서 모든 곳에 들러서 개수를 담고 들린곳은 전부 이미 들른곳이라는 표시를 해주자.
검색조건 -> 오른쪽 또는 아래 (좌->우, 상->하로 서칭하기 때문에 최초 지점에서 우측과 하단으로 처음에 뻗어나가야 한다.)

* 배운점
DFS 함수를 작성할 때 global num을 활용하면 들른 dfs의 개수를 확인할 수 있다.
그리고 예외의 경우 (그래프 밖에 도착한 경우) return문만 써주면 된다.
heap 형태에서 unpacking을 할 경우 힙 트리가 출력되므로 minheap 순서대로 출력하기 위해서는 sort를 해주거나 while문으로 heappop을 해주자.
"""
# 내 풀이
import sys
import heapq
input = sys.stdin.readline
n = int(input())
MAP = [list(map(int, list(input().rstrip()))) for _ in range(n)]
ans, num = 0, 0
ans_arr = []


def dfs(x, y):  # i와 j의 좌표를 가지고 dfs 진행하기
    global num  # 갯수를 담아서 리턴한다. 글로벌을 사용해서 초기화를 시켜주는 방법을 써야하나?
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return  # 이 경우 아무것도 안한다.
    if MAP[x][y] == 1:
        MAP[x][y] = 0
        num += 1
        dfs(x, y-1)  # 상
        dfs(x, y+1)  # 하
        dfs(x-1, y)  # 좌
        dfs(x+1, y)  # 우
        return num
    # 오지 않을 경우 여기서 return 문 작성?? 모르겠다


for x in range(n):
    for y in range(n): # n * n 형태여서 가능함
        if MAP[x][y] == 1: 
            heapq.heappush(ans_arr, dfs(x,y))
            num = 0
            ans += 1

print(ans)
while ans_arr: print(heapq.heappop(ans_arr))
