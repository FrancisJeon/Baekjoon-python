# DFS와 BFS 211018 다시풀기
""" 
예전에 풀다가 답 복붙했고 1018 다시 시도하는중

규칙 -> 방문 정점 여러개일 경우 번호가 작은걸 먼저 들린다.
* visited를 따로 설정하지 않은 케이스
1) BFS는 큐 DFS는 스택
2) 주어진 정보를 dict[k] += [v]를 해줬는데 이제 양방향으로 dict[v] += [k] 도 해주는 방법으로 바꿨다.
3) defaultdict를 사용해서 만드는게 가독성과 예외처리에 유리
4) visited를 미리 만들어서 사용했는데 visited를 함수에 빈 리스트로 넣어서 not in 으로 체크하거나 set로 빼주는 방법도 좋음
* visited를 만든 케이스
1번 정답에 있는데 그래프를 생성할 때 딕셔너리가 아닌 0번에 []를 담은 2차원 배열로 생성해주었다.

4 5 1
1 4
1 3
1 2
2 4
3 4
"""
# 구글링 정답, 속도가 장점이고 visited 리스트를 활용하는 방식이 맘에들었다.
import sys
from collections import deque


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, sys.stdin.readline().split())
# 노드 개수보다 하나 많은 텅빈 그래프 만들기 여기서 graph[0]은 쓰레기값
graph = [[] for _ in range(n+1)]

for _ in range(m):                      # 입력 받아서 그래프 만들기
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):                      # 각 노드에서 연결된 '간선' 오름차순으로 정렬
    graph[i].sort()


visited = [False]*(n+1)                 # 각 노드의 방문여부를 표현
dfs(graph, v, visited)
print()
visited = [False]*(n+1)                 # 각 노드의 방문여부를 표현
bfs(graph, v, visited)



# 2번, 정석 dfs, bfs로 visited = [0] * (n+1)을 사용하지 않은 방법
# import sys
# from collections import defaultdict
# from collections import deque
# input = sys.stdin.readline
# adj_list = defaultdict(list)

# n, m, s = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작 정점 번호
# for _ in range(m):
#     k,v = map(int, input().split())
#     adj_list[k] += [v]
#     adj_list[v] += [k]
# # print(adj_list) # 인접리스트로 연결된걸 확인 딕셔너리 내부에서 연결된걸 확인 -> sorting이 필요하다.
# # for i in adj_list: adj_list[i]
# # print(adj_list) # sorting 확인, DFS에서는 pop을 해주기 위해선 역순으로 해야한다. 하지만 BFS에서는 정렬 순서가 반대로 돼야 문제가 요구하는 방향으로 돌아간다. -> sorting을 두번의 케이스 별도로 해주기


# def dfs(graph, start_node):
#     visited = []
#     stack = [start_node]
    
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.append(node)
#             if node in graph:
#                 temp = list(set(graph[node])-set(visited))
#                 temp.sort(reverse=True) 
#                 # 역순으로 sorting해서 넣으면 [4, 3, 2] 이렇게 담겨서 pop 할때 작은 값이 먼저 나온다.
#                 stack += temp
#     return visited

# def bfs(graph, start_node):
#     queue = deque([start_node])
#     visited = []
    
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.append(node)
#             if node in graph:
#                 temp = list(set(graph[node])-set(visited))
#                 temp.sort()
#                 queue += temp
#     return visited

# print(*dfs(adj_list, s))
# print(*bfs(adj_list, s))
