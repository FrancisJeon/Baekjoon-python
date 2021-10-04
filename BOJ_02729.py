# 01000001 이진수 덧셈
""" 
n 개의 입력값
각 입력값은 이진법 숫자 2개가 주어진다.
두개를 합친 값을 이진법으로 출력하기
"""
# 내장함수 사용 >> 직접 구현할 필요 없다고함
def solution(n):
    for _ in range(n):
        a, b = map(str, input().split())
        print(bin(int(a, 2) + int(b, 2))[2:])
        # int(a, 2) 대신 bin을 사용해보겠다. 안된다

n = int(input())
solution(n)

