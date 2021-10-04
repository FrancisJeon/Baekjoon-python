import itertools
import sys

inp = sys.stdin.readline
n, k = map(int, input().split())

""" lst_a = list(range(n+1))
permu_a = list(itertools.permutations(lst_a, k))
cwp_a = list(itertools.combinations_with_replacement(lst_a, k))

answer = set(permu_a) | set(cwp_a)
cnt = 0
for i in answer:
    if sum(i) == n:
        cnt += 1
print(cnt % 1000000000) """
### 메모리 초과 

# n을 만드는데 k번 더해야함 요소는 0~n 사이의 숫자들로 구성
# k -> k-1 -> k-n -> 1
# 0 -> 0 -> ......-> n
