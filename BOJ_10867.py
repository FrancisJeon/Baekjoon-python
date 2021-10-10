# 중복 빼고 정렬하기 211008
""" 
N개의 정수를 오름차순으로 정렬하는데 같은 정수는 한번만 출력한다.
set 활용이 제일 만만해보인다.
"""
# import sys
# input = sys.stdin.readline
# input()
# arr = sorted(set(map(int, input().split())))
# print(*arr)

# 숏코딩
input(); print(*sorted(set(map(int, input().split()))))