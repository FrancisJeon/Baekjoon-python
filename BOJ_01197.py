# 최소 스패닝 트리 211006
""" 
입력
V E - 정점의 개수 간선의 개수
a b c - 정점 a와 b가 c 가중치로 연결되어 있다. -> 간선의 개수만큼 반복
3 3
1 2 1
2 3 2
1 3 3
-> 3
* 알고리즘
1. n 개의 s e c 노드입력을 받는다.
2. 정점의 개수(v)만큼 시작점부터 거리를 측정하는 리스트가 필요하고 [INF] * (v+1), 간선의 개수만큼의 queue작업이 필요하다.
# 최소신장트리는 어느 점에서 시작하던 결과물의 가중치가 동일하다고 한다. 그래서 정점이 1부터 시작하니까 1로 잡기로

"""
# 1. 메모리 초과 - 프림도 아니고 BFS에 가까운듯 하다.
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

v, e = map(int, input().split())
tree_dict = defaultdict(list)
cost = [int(1e9)] * (v + 1)

for _ in range(e): # 간선 개수 e
    s, e, c = map(int, input().split())
    tree_dict[s].append((e, c))
# 1번 정점은 무조건 존재해야 하므로 1번의 정점에 0 cost를 준 상태로 시작
queue = deque([(0, 1)]) # cost는 0, 위치는 1
while queue:
    c, n = queue.popleft() # cost와 노드
    cost[n] = c
    for i, j in tree_dict[n]:  # n과 연결된 모든 애들을 queue에 넣어야함 그리고 cost와 비교도 해야한다.
        # i는 노드, j는 cost
        if cost[i] < j:
            cost[i] = j # 바꿔주기
        queue.append((j, i)) 
        # 이때 간선 정보는 INF, 0, 1(2노드), 3(3노드) 그리고 2와 3을 큐에 담아야한다. cost가 앞에가도록 (앞에 굳이 갈 필요는 없겠다..)
print(sum(cost[1:]))
'''
# 2. 크루스칼 알고리즘
""" 
1. 루트를 저장하는 Vroot 배열을 생성. (root는 연결요소 중 값이 가장 작은값)
2. 간선들을 가중치 기준으로 정렬한다.
3. 간선들이 이은 두 정점을 find 함수를 통해 두 root를 찾는다. (sRoot, eRoot)
4. 두 root가 다르다면 큰 값을 작은값으로 만들어 연결되게 해준다.
5. 가중치를 더한다.
"""
import sys
input = sys.stdin.readline

V,E = map(int, input().split())
Vroot = [i for i in range(V+1)] # 0~V가 담긴 배열
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))
Elist.sort(key=lambda x: x[2]) # 비용이 적게드는 순으로 정렬

# Vroot 내부에 x번 인덱스에는 x라는 숫자가 담겨있다. 만약 다른 경우라면 다른 인덱스에 먹힌것
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot: # cost 순으로 정렬된 상태에서 Elist이므로 (1, 2, 1), (2, 3, 2), (1, 3, 3) 순으로 순회한다.
        if sRoot > eRoot: 
            # 시작점이 더 높은 순위라면 낮은순위로 덮어씌우기
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w # w코스트 넣어주기
        # 처음 값은 w가 1, 두번째는 2로 3이 출력된다. 1 3 3 에서는 이미 같은 숫자로 변해서 answer에 추가없음
print(answer)