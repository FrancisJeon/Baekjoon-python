# 첼시를 도와줘 211005
""" 
입력되는 선수 중 제일 비싼 선수를 출력하자

* 1. 입력 받을 때 모든 값을 담아서 sorting을 하는 방법
* 2. 받을 때 마다 max를 비교해서 max 선수가 담길 때 이름을 담아주는 방법 -> 이 방법을 사용할 예정
"""
# 1. 입력마다 max를 비교 -> 68ms(sys), 308ms(sys X)
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     max_cost = -1e9
#     ans = ''
#     for __ in range(int(input())):
#         cost, name = input().split()
#         if int(cost) > max_cost:
#             max_cost = int(cost)
#             ans = name
#     print(ans)

# 2. 모든 값을 담아서 sorting
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    array = sorted([(input().split()) for _ in range(int(input()))], key = lambda x: -int(x[0]))
    # array = sorted(array, key = lambda x: -int(x[0]))
    print(array[0][1]) # 마지막에 담긴 값의 name 부분
