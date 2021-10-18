# 전투 211018
""" 
W는 내 병사, B는 상대 병사
그래프가 주어지면 연결된 병사들의 전투력의 합을 출력하기 전투력은 N명^2

* 알고리즘
연결된 모든 병사들의 합을 계산하기 -> 한번 계산한 애들은 1로 바꿔주기
W는 W끼리 합치고 B는 B에 += 시키고 마지막에 W, B 프린트

6 4
WWWWWW
BBBBBB
WWWWWW
BBBBBB
"""
n,m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
ans = 0
w_pow = 0
b_pow = 0

# dfs로 파워 리턴시키기
def dfs(x, y, team):
    global ans
    if x <= -1 or m <= x or y <= -1 or n <= y:
        return # x나 y가 그래프 밖으로 나온 케이스는 빠져나오기
    if graph[x][y] == team:
        graph[x][y] = 1
        ans += 1
        dfs(x, y-1, team)
        dfs(x, y+1, team)        
        dfs(x-1, y, team)
        dfs(x+1, y, team)
        return ans

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            w_pow += dfs(i,j, 'W') ** 2
            ans = 0
        if graph[i][j] == 'B':
            b_pow += dfs(i,j, 'B') ** 2
            ans = 0
print(w_pow, b_pow)