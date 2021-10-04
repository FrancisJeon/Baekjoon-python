# 테스트용 코드
from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
commons = set('antatica')
arr = [set(input().rstrip()) - commons for _ in range(n)]
ts = sorted(set(chr(c) for c in range(ord('a'), ord('z') + 1)) - commons)
# print(ts) # 'b','d','e' ... 'z'
ts = [1 << ord(c) - ord('a') for c in ts]
# print(ts) # 2 8 16 ....

res = 0
arr = [sum(1 << ord(c) - ord('a') for c in y) for y in arr]
# arr은 기본단어 제외한 단어들로만 구성된 상태인데 그걸 비트연산 시킨 형태로 만듬.

print(arr)
for z in [sum(t) for t in (combinations(ts, k - 5) if k >= 5 else ())]: # itertools의 조합들을 만들어준 뒤    
    res = max(res, sum((z&y) == y for y in arr))
    # z = 10 18 34 66 ..... 2개로 만들 수 있는 모든 조합
    # z&y == y -> y는 2, 120
    for y in arr:
        print(f'z&y = {bin(z&y)}', end = ' ')
        print(f'y = {bin(y)}, z = {bin(z)}')

    # res = max(res, sum((z & y) == y for y in arr))
    


