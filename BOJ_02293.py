# 동전 1 211007 -> 211015
""" 
n가지 동전으로 합이 k원이 되게 만드는데, 조합의 갯수를 출력하라.
같은 동전을 여러개 사용해도 된다.

* 알고리즘 211007
//가장 작은 동전부터 꽉 채운 경우의 수를 만들자 (sort)
//ex) 1이 들어간 경우 1*10, 1*8 2, 1*5 5, 1*3 2 5 (나머지 동전은 한개만?)
//2가 들어간 경우 2 1*8, 2*2 1*6, 2*3 1*4, 2*4 + 1*2, 2*5
//5가 들어간 경우 5 1*5, 5 1*3 2, 5*2
//이 중 겹치지 않는 경우의 수를 합친다.
//[1*10, 1*8 2, 1*6 2*2, 1*5 5, 1*4 2*3, 1*3 2 5, 1*2 2*4, 2*5, 5 1*3 2, 5*2]
//1*? 2*? 3*?를 만드는데 가능한 내림차순으로 만들기 (2번, 3번 동전도 최대한 갯수를 넣어서)
//1*0 2*5 3*0/ 1*0 2*1 3*1 이런식으로
* 다이나믹 프로그래밍 211015
동전의 종류가아닌 목표가격을 기준으로 프로그램을 짜야 한다.
동전이 1, 2, 5원일 경우
1원 = 1
2원 = 1 + 1 , 2
3원 = 1 + 1 + 1, 2 + 1
4원 = 1 + 1 + 1 + 1, 1 + 1 + 2, 2 + 2
5원 = 1 + 1 + 1 + 1 + 1, 1 + 1 + 1 + 2, 1 + 2 + 2, 5
.....
점화식..?
(1) - 1원
(2) - dp(1원) + dp(1원) / dp(2원)
(3) - dp(1원) + dp(1원) + dp(1원) / dp (1원) + dp(2원)

* 문제의 핵심
# 1
전체의 문제를 부분 문제로 잘 나누었는가? 그렇다면 부문 문제의 점화식은 무엇인가?
부분 문제들을 해결하며 얻는 결과값을 메모이제이션 하는가?
부문 문제의 점화식은 부문문제들 사이의 관계를 빠짐없이 고려하는가?
# 2
#1을 바탕으로 할 때 문제의 핵심은 다음과 같다.
가치의 합이 k원이 되는 경우의 수를 구하는 문제를 가치의 합이 i원이 되는 부문문제로 나눈다.
특정 동전을 썼을 때 가치의 합이 i원이 되는 경우의 수를 구하는 부분문제로 나눈다.
"""

# 정답코드
n, k = map(int, input().split())
c = [int(input()) for i in range(n)]
dp = [0 for i in range(k+1)]  # k+1 사이즈를 선언
dp[0] = 1  # 인덱스 0은 동전 1개만 쓸 경우를 고려하기 위해 선언

for i in c:  # 동전 종류 빼주기
    for j in range(i, k+1):  # 해당 금액의 동전부터 시작하기 위함
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[k])