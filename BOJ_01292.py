# 쉽게 푸는 문제 210928
""" 
1 한번 2 두번 3 세번 .... 수열에서 일정 구간 A, B <= 1000이 주어지면 그 숫자들의 합을 구하기
1000개의 숫자들...
"""
A, B = map(int, input().split())
arrs = []; i = 1
while len(arrs) < B:
    arrs += [i] * i; i += 1
print(sum(arrs[A-1:B]))
