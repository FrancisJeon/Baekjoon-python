""" 210616 20:14 항해 15번 QED """
###----- 진짜 약수 -----###
# A가 N의 진짜 약수가 되려면 N = A*x
# A!=1 || A!=N
# input = 첫줄. N의 진짜 약수의 갯수
# 두번째줄. N의 진짜 약수가 주어진다.
# output = 첫줄. N 출력
import math 

num = int(input())
denom = list(map(int, input().split()))
denom.sort()
ans = denom[0] * denom[-1]

print(ans)