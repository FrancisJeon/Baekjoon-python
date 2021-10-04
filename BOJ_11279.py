# 최대 힙 210926
""" 
n개의 연산 갯수 주어지고
x가 자연수라면 배열에 x를 넣고 0을 넣을경우 가장 큰 값을 출력하고 배열에서 제거한다
"""
import heapq
import sys
input = sys.stdin.readline

h = []

for _ in range(int(input())):
    x = -int(input()) # 음수 값으로 해야 최대 힙이 나온다
    if x == 0: print(-heapq.heappop(h)) if h else print(0)
    else: heapq.heappush(h, x)

