# 구글에서 답을 찾아서 복붙했다.
n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for i in range(n+1)]
# matrix 변수에 [0]이 노드갯수+1인 형태로 생성 ------- #
# 0으로 초기화된 노드이고 n+1로 생성해서 인덱스를 편하게 하려는 듯하다.
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0]*(n+1)
# 노드 갯수만큼 반복하면서 matrix의 간선부분을 1로 바꿔주었다.
# visit_list는 0을 n+1개만큼 반복해서 1차원 리스트로 생성해준다. 마찬가지로 인덱스를 바로 넣어주기 위해 +1을 넣어준듯 ------- #
def dfs(v):
    visit_list[v] = 1  # 방문한 점 1로 표시
    print(v, end=' ')
    for i in range(1, n+1):
        if(visit_list[i] == 0 and matrix[v][i] == 1):
            dfs(i)
    # 1부터 n+1까지 i를 반복하면서 방문하지 않았고 matrix의 간선이 있을 경우 dfs를 재귀로 한번 더 들어가준다.

def bfs(v):
    queue = [v]  # 들려야 할 정점 저장
    visit_list[v] = 0  # 방문한 점 0으로 표시. 초기화 없이 앞에서 해준 값에서 이어주려고? -> 맞다.
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if(visit_list[i] == 1 and matrix[v][i] == 1):
                queue.append(i)
                visit_list[i] = 0
    # queue가 비지 않았을 경우 0번인덱스를 pop 해주고 (popleft) 그 값을 v로 받는다.
    # 그 다음 1~n+1사이의 i가 visit_list 방문한 리스트도 1이고 matrix도 1일 경우 visit_list 0으로 만들고 queue에 더해준다. 반복문 돌리기
    # (DFS에서 1로 만들어줬기 때문에 0으로 만드는것 같다.) 

dfs(v)
print()
bfs(v)
