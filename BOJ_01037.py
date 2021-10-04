""" 210616 20:14 항해 15번 QED 약수"""
###----- 진짜 약수 -----###
# A가 N의 진짜 약수가 되려면 N = A*x
# A!=1 || A!=N
# input = 첫줄. N의 진짜 약수의 갯수
# 두번째줄. N의 진짜 약수가 주어진다.
# output = 첫줄. N 출력

# 1차 
"""
num = int(input())
denom = list(map(int, input().split()))
denom.sort()
# ans = denom[0] * denom[-1]
# print(ans) 
print(denom[0] * denom[-1])
"""

# 2차
num = int(input())
denom = list(map(int, input().split()))
print(max(denom) * min(denom))
# max, min 함수를 쓰면 sorting 하는것보다 시간이 오래걸림