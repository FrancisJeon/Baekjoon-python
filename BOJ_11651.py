""" 210617 12:44 항해 20번 QED """
# 2차원 평면 위의 점 N개 좌표를 낮은 y좌표를 가진 점부터 출력 같은 y값을 가진 경우 더 낮은 x좌표 먼저 출력하는 프로그램
# 입력값
# 점의 갯수 n줄
# 점의 좌표 - n개

# 정렬 순서 = y좌표가 가장 작은곳부터 같을 때는 x좌표가 낮은게 우선
import sys 
n = int(sys.stdin.readline())

orderCoor = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    orderCoor.append([y, x])

orderCoor.sort()
for i in orderCoor:
    print(i[1], i[0])
