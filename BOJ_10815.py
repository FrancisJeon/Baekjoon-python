# 숫자카드 211008
""" 
입력
N 가진 카드 수
카드 종류 공백으로 구분
M 찾을 카드
카드 종류 공백으로 구분
출력
한줄로 M이 N에 있는지 유무 1, 0
"""
# 1번 for i in arr -> 700ms
# import sys
# input = sys.stdin.readline

# n = input()
# arr_n = set(input().split())
# m = input()
# arr_m = list(input().split())

# for i in arr_m:
#     print(1 if i in arr_n else 0, end=' ')

# 2번 bisect_left -> 1416ms
# import sys
# import bisect
# input = sys.stdin.readline

# n = int(input())
# arr_n = sorted(map(int, input().split()))
# m = input()
# arr_m = list(map(int, input().split()))

# for i in arr_m:
#     # print(bisect.bisect_left(arr_n, i), end = ' ')
#     print(0 if bisect.bisect_left(arr_n, i) == n or arr_n[bisect.bisect_left(arr_n, i)] != i else 1, end=' ')

# 3번 정석 이분탐색 -> 3096ms
import sys
input = sys.stdin.readline

n = int(input())
arr_n = sorted(map(int, input().split()))
m = input()
arr_m = list(map(int, input().split()))

def bin_src(i):
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if arr_n[mid] == i:
            return True
        if arr_n[mid] > i:
            r = mid - 1
        else:
            l = mid + 1

for i in arr_m:
    print(1 if bin_src(i) else 0, end=' ')
