""" 210618 18:02 항해 27번 """
import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    answer = math.factorial(m) / (math.factorial(n) * math.factorial(m-n))
    print(int(answer))