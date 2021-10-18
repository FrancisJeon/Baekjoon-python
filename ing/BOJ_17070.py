# 파이프 옮기기 211016
""" 
조건
파이프는 밀면서 한번에 45도만 회전가능, 처음엔 (1,1)과 (1,2)를 차지하고 있다.
파이프는 앞부분(1,2)을 진행방향으로 민 다음 방향전환을 해야 한다. 1은 벽이고 처음에 밀었던 부분이 벽에 닿으면 안된다. (3x3 케이스에서 보면 집 외벽을 뚫고 나가는 경우는 인정해주는 듯 하다)
* 입력
N (집의 크기)가 주어지고
집의 상태가 주어진다. (N만큼 반복 입력)
* 출력
N,N 까지 도달하는 경우의 수

"""
# DP로 맵을 구현하고 가로, 세로, 대각선 모양으로 도착했는지에 따라 별도의 맵에 저장하는 방식
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 0: 가로로 온 수 / 1: 세로로 온 수 / 2: 대각선으로 온 수
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
i = 2
while i < n:
    if arr[0][i]:
        break
    dp[0][0][i] = 1
    i += 1

for i in range(1, n):
    for j in range(2, n):
        if arr[i][j] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][-1][-1] for i in range(3)))
