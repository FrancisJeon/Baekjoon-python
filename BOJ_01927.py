# 최소 힙 210927
import sys
import heapq
input = sys.stdin.readline

def min_heap(arr):
    h = []
    for i in arr:
        if i:
            heapq.heappush(h, i)
        else:
            print(heapq.heappop(h) if h else 0)

arr = [int(input()) for _ in range(int(input()))]
min_heap(arr)