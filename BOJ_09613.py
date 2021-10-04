# sum of gcd 210927
"""
test case 갯수만큼의 입력이 주어지고
그 후 입력값들은 
m -> 뒤에 주어진 수의 갯수
*arr -> m개의 수
arr에 있는 수들의 합으로 최대공약수를 구하자
호제법
a를 b로 나누고 나머지가 0이 아니면 b를 a%b로 나눠주는 방법을 반복해준다.
모듈러가 0이될 때 나눠준 값인 b부분이 최대공약수

"""
from itertools import combinations
def gcd(a, b):
    # 큰 수가 a로 가도록 swap 해주기
    if b > a: a, b = b, a
    if a % b == 0: return b
    else:
        new_a, new_b = b, a % b
        a, b = new_a, new_b
        return gcd(a,b) # 여기서 return을 적어줘야 재귀로 들어가서 정상적인 값이 출력

def solution(n):
    for _ in range(n):
        # gcds = []
        m, *arr = map(int, input().split())
        # pair를 만들기 위해서 brute force로 모든 조합을 찾아야 하므로 combinations를 사용하겠다.
        cb = list(combinations(arr, 2))
        # for a, b in cb:
        #     gcds.append(gcd(a,b))
        # 25, 29~30 줄 합친 리스트컴프리핸션
        gcds = [gcd(a,b) for a,b in cb]
        print(sum(gcds))
                
n = int(input())
solution(n)

