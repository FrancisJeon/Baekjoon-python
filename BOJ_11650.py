# 좌표 정렬하기 211001
""" 
n이 주어지고 
n개의 좌표가 주어질 때 정렬한 결과를 출력한다.
x좌표, y좌표 오름차순으로 정렬
"""
import sys
input = sys.stdin.readline
xy = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    xy.append((x, y))
for x, y in sorted(xy, key=lambda x: (x[0], x[1])): # 람다 없이 sorted 하는게 더 빠르다
    print(x, y)
