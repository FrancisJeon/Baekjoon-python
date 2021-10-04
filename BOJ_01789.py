# 수들의 합
""" 서로 다른 N개의 자연수의 합이 S가 된다면 N의 최대 값을 구하기(len)
즉 sum(a, b, c....n) = 200, max(len()) ?
1, 2, 3, 4, 5, 6, 7, 8, 9, 10... 최대한 작은 수 부터 넣는게 가장 많이 넣을 수 있다.
만약 마지막 숫자를 넣으면 목표를 초과하는 경우 목표와 마지막 숫자의 차이에 해당하는 숫자를 빼고 본인을 넣어준다..
* 1. sum 을 반복해서 사용하면 -> 시간초과
* 2. sum 대신 카운터와 sum_of_i를 담은 숫자 두개를 이용한다 -> 마지막에 틀린 케이스 나옴
* 2-2. 2번에 딱 맞게되는 조건도 추가
"""
# 정답 코드 -> 단축 가능
# s = int(input())
# n = 0 # 카운터
# sum_of_i = 0 # sum

# for i in range(1, s):
#     if sum_of_i + i < s:
#         sum_of_i += i
#         n += 1
#     elif sum_of_i + i > s:
#         # 이 때는 더이상 계산할 필요 없이 n에서 하나 빼고 하나 넣어줘서 이 값이 카운터로 나올 것 같다.        
#         break
#     elif sum_of_i + i == s:
#         n += 1
#         break
# print(n)
# 단축코드
s = int(input())
sum_of_i = 0
for i in range(s+1):
    sum_of_i += i
    if sum_of_i >= s:
        print(i if sum_of_i == s else i-1)
        break



# 다른 정답 코드
'''
N = int(input())
sum = 0
for i in range(N+1):
    sum += i
    if sum >= N:
        print([i, i-1][sum > N])
        # print(i-1 if sum > N else i)
        # 프린트 내부에 [i, i-1][sum > N]은 무슨 의미일까?
        # [i, i-1]은 각각 False와 True 시 출력되는 조건이다. 즉 print(i-1 if sum > N else i)와 같다.
        break
'''

