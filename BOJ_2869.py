""" 210616 19:50 항해 14번 QED """
import math

a, b, v = map(int, input().split())

# a*day -b*day + a <<가 도달하는 순간의 day 구하기
# v-a까지 도달하는 날짜 + 1일?
# 올림으로 올려줘야 0.25로 day가 나오는경우 1일로 인식해준다.

height = (v - a)
day = math.ceil(height/(a-b))
day += 1
print(day)