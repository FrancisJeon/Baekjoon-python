# 최소비용 구하기 211005
""" 
입력
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)
둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)
셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
출력
출발-도착까지 최소비용
* 알고리즘
최단거리 or 방문하지 않은 경우를 들른 뒤 최단거리 업데이트하기
## 시작도시, 끝도시, 비용 3 정보를 활용해서 딕셔너리 형태로 연결시킬까? 
    # 1: [(2, 2), (3, 3), (4, 1), (5, 10)], 2: [(4, 2),], 3: [(5, 1)], 4: [(5, 3)]
    이 방법 자체는 틀리지 않았는데 defaultdict를 활용해서 만들자

# 답을 보고 작성하였으나 다익스트라 알고리즘과 queue를 활용한 방법은 그대로 익혀야겠다.
코드중에선 아래의 코드가 제일 직관적

"""
# 입력값 처리 -> 리스트 컴프리헨션으로 s,e,c 정보를 하나의 리스트로 담았다가 바로 정보에 대한 처리를 하는게 더 효율적이라 코드 변경했다.
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
graph = defaultdict(list)
distances = [1e9] * (n +1)

n = int(input()) # 도시 개수
for i in range(int(input())): # 출발, 도착, 비용 목록
    s,e,c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split()) # start, end 도시 

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # queue에 처음 넣는 정보는 (자기 자신과의 거리 0, 시작위치)
    
    while queue:
        # start에서 최소의 distance를 기준으로 heappop 해준다.
        dist, now = heapq.heappop(queue)
        if distances[now] < dist: # 입력받은 distance 보다 현재 거리가 더 낮다면 그대로 다음 큐로
            continue
        for node in graph[now]: # 그래프에서 현 위치의 연결포인트들
            cost = dist + node[1] # [1] 번 인덱스는 cost를 의미한다 [0] 인덱스는 연결된 도착위치
            if distances[node[0]] > cost:
                # 만약 이번에 든 비용보다 기존의 비용이 더 크다면 업데이트
                distances[node[0]] = cost 
                heapq.heappush(queue, (cost, node[0])) # 힙에 넣어준다. 다음 장소 탐색을 위해

dijkstra(start)
print(distances[end])
