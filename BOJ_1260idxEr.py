""" 220622 19:30 항해 32번 DFS와 BFS """
'''
아이디어: 
* 근접노드를 담아두는 N 길이의 2차원 배열을 생성하기
* 노드가 입력될 때 값을 뒤집어줘서 2차원 배열에 해당 인덱스에 넣어주기
* visited 리스트를 만들어서 이 안에 없을 경우 들르게 하기
'''
import sys
from collections import deque
inp = sys.stdin.readline

n, m, v = map(int, inp().split())
adj_nodes = [[] for i in range(n)]
dfs = deque()
bfs = deque()

for _ in range(m): # 인접노드 완성시키기
    adj_node = list(map(int, inp().split()))
    adj_nodes[adj_node[0]-1].append(adj_node[1])
    adj_nodes[adj_node[1]-1].append(adj_node[0])

[i.sort() for i in adj_nodes] # 들어온 값 sort로 작은 값이 앞에 가게 정렬

# DFS
visited = list()
dfs.append(v) # stack (빼주면서 visited로 옮긴다.)

'''강의 코드 따라친 블록'''
# dfs_nodes = adj_nodes[::-1]
# while dfs:
#     current_node = dfs.pop()
#     visited.append(current_node)
#     for i in adj_nodes[current_node-1]:
#         if i not in visited:
#             dfs.append(i)

# 시작점 v에서 DFS 수행
visited.append(v)
while len(visited) != n and len(dfs) != 0: 
    # visited가 n 만큼 되는 순간 모든 노드를 들른것으로 보고 탈출. 또는 더이상 갈수 있는곳이 없다면 탈출
    for i in adj_nodes[dfs[-1]-1]: # 현재 노드의 주변노드를 기준으로 안들린곳을 탐색하기
        for j in adj_nodes[i]:
            if j in visited:
                continue
            visited.append(j)
            dfs.append(j)
            break
        
        dfs.pop()
        # 다 들른 경우에 길이 없으면 뒤로 돌아나가면서 전 노드로 이동 (이 때 뒤로 돌아가는게 바로 pop을 해버리면서 전전단계로 돌아간다)
    
[print(i, end=' ') for i in visited]
print()

# BFS
visited = list()
bfs.append(v)
visited.append(v)

while len(visited) != n and len(bfs) != 0:
    for i in adj_nodes[bfs[0]-1]:
        if i not in visited:
            visited.append(i)
            bfs.append(i)
    
    bfs.popleft()
    # 더 갈곳이 없을 때 그 값을 popleft 시켜주기
        
[print(i, end=' ') for i in visited]