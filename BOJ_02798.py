""" 210820 블랙잭 항해 39번 QED """
"""  
각 카드에 양의 정수가 쓰여 있고 N장의 카드를 숫자가 보이게 바닥에 두면 M을 크게 외친다.
플레이어는 M을 넘지 않고 최대한 가깝게 만들어야 한다.
입력 -> 
첫째줄에는 N, M이 주어진다.
둘째 줄에는 카드에 쓰인 수가 주어진다.
출력 -> M에 최대한 가까운 카드 3장의 합을 출력한다.
브루트포스? 전수조사라고도 부른다. 원시적으로 문제를 푸는 노가다의 학술적 버전이다.
내 풀이는 sorting을 해준 다음 3중 for문을 사용했는데 정답지 풀이들을 보니까 그냥 sort 없이 다 더해준 다음 m보다 같거나 작은 값만 사용했다.
"""
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
cards = sorted(list(map(int, input().split())), reverse = True)
result = 0

for i in range(n):
    for j in range(i+1, n):
        if cards[i] + cards[j] >= m:
            continue
        
        for k in range(j+1, n):
            sum = cards[i] + cards[j] + cards[k] 
            if sum <= m:
                result = max(result, sum)
                if result == m:
                    print(result)
                    sys.exit()
print(result)
