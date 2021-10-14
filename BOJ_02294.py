# 동전2 211014
""" 
동전1과 유사하지만
경우의 수가 아닌 동전의 최소 개수를 출력해야 하고 (개수 기록) 출력이 불가능할 경우 -1을 출력한다.

* 여전히 다이나믹 프로그래밍 이지만 최소 개수만 최신화 해주면 된다.
3 15 n, k
1 5 12 coin[]
dp(1) - 1
dp(2) - 2 # 1+1
dp(3) - 1 # 3
dp(4) - 2 # 3+1

동전을 반복하면서 [n] 을 채워준다.
1원을 기준으로 1, 2, 3, 4, 5 ... 이렇게 채워진다.
그 다음 3원을 기준으로 3원에 3값이 1로 변화한다. 4원에서는 [1]이 -1이 아니라면 그 값과 자기자신의 개수를 합친 개수를 넣어준다.
처음에는 -1을 넣어주었으나 여기선 limit으로 초기화를 두는게 푸는 방법에 더 맞았다.
"""
# 내가 생각했던 코드가 다 틀렸다 ㅋㅋ 동전1과 비슷하지만 처음 값에 0을 넣어주고 개수를 측정하는 방식이다. 
# 468ms, sys로 input 바꿔도 무의미함
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# coin = [int(input()) for _ in range(n)]
# limit = 10001
# dp = [0] + [limit] * k
# for i in coin: # 코인을 반복해주면서 돌려주고
#     for j in range(i, k+1): 
#         dp[j] = min(dp[j], dp[j - i] + 1) 
#         # dp[j-1] + 1은 dp[0]에 0개를 두고 본인의 값과 일치하는 index에 1개를 넣어주기 위함. 
#         # 또한 기존의 dp값이 존재한다면 그곳에 이번에 더해질 자신의 코인 한개를 더한 값을 넣어준다.
# print(dp[k] if dp[k] != limit else -1)


# 168ms 정답
import sys
input = sys.stdin.readline

def sol2294():
    n, k = map(int, input().split())
    coins = set([int(input()) for _ in range(n)]) # 동전은 set로 받아주고
    min_coin = min(coins)
    
    visited = [False] * (k + 1)
    cost = [k]
    answer = 0
    while cost: # while문을 이용, cost는 [k]로 처음 입력한 금액이 담겨있다.
        answer += 1
        u = [] # u 로 빈 리스트를 생성해두고
        for c in cost:
            for coin in coins:
                val = c - coin
                if val == 0: # 남은 금액과 coin의 차가 딱 떨어지면 1을 반납
                    return answer
                if val >= min_coin and not visited[val]:
                    u.append(val)
                    visited[val] = True
        cost = u # 새로운 리스트가 cost를 대체한다.
    return -1
# 디버그
# u = [14], [14, 3], [14, 3, 10] -> cost = [14, 3, 10]
# u = [13], [13, 2], [13, 2, 9], [13, 2, 9, 5] -> cost = [13, 2, 9, 5]
# u = [12], [12, 1], [12, 1, 8], [12, 1, 8, 4] -> 이게 만들어지는 순간의 c는 5, coin에서 5가 뽑힌다.

if __name__ == '__main__':
    print(sol2294())
