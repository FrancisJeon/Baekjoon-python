# 감소하는 수 211015
""" 
N번째 감소하는 수 출력하기
0 1 2 3 4 5 6 7 8 9 -> 10개의 감소하는 수
11번째 20, 12번째 21, 13번째 30, 14번째 31, 15번째 32, 16번째 40, 17번째 41, 18번째 42
N은 100만번째.. 종료조건을 잘 만들어서 메모이제이션까진 필요없을 듯 메모리 낭비
* 알고리즘
특정 자리가 감소하는 수가 되기 위해서는 자릿수와 그 다음 수를 계산해야 한다.
브루트포스에 백트랙킹이라고 해서 그냥 무식한 방법으로 먼저 풀 예정인데.. DP를 활용할 수 있을것 같다는 생각이 든다.
1. 숫자를 받은 뒤 list(str(number)) 를 해주면 숫자가 리스트로 변해서 자리수를 비교하기 편하다. 이를 활용해서 감소하는 수인지 확인하는 함수를 만들자 -> 시간초과 발생
2. n번째 감소하는 수가 없다면 -1을 출력하라고 하는데 이해가 안가서 답지를 살펴봤고 가능한 최고로 높은 수가 9876543210이라서 이 수를 넘는 n이 입력되면 -1을 출력해야 한다.

"""
# is_desc 함수 활용 -> 시간초과, 1부터 계산하는 방법은 시간초과가 발생한다.
""" 
from collections import deque
n = int(input())
ans = 0
num = 0

def is_desc(number):
    check = deque(map(int, list(str(number)))) # 성공적으로 리스트 생성 완료
    a = check.popleft() # 왼쪽 수를 빼서 비교 대상으로 두자
    while check: 
        b = check.popleft()
        if b >= a:
            return False
        a = b # 비교를 위한 값이 덮어씌워진다.
    return True    
    
# 1번째 ~ n번째 까지 반복문을 돌려주고 수는 계속 증가시키면서 저장해줘야 한다.
while ans < n:
    if is_desc(num):
        ans += 1
    num += 1
print(num)
"""

# 조합을 활용한 방법, 80ms
# combination을 활용해도 속도가 빠른 편이고 try, except 구문을 활용한 방법도 맘에 들었다.
from itertools import combinations
n = int(input())
num = []         # 모든 감소하는 수
for i in range(1, 11):  # 1~10개의 조합 만들기 (0~9개니깐)
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        num.append(int("".join(map(str, comb))))
try:
    print(sorted(num)[n]) # 오름차순
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)
