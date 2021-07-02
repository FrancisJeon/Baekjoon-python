""" 210618 00:03 QED """
import sys
import math

n, k = map(int, sys.stdin.readline().split())

ans = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
print(int(ans))