# 단어 공부 210926
# import sys
from collections import Counter
# input = sys.stdin.readline
a = input().upper()
if len(a) == 1: print(a)
else: print("?") if Counter(a).most_common()[0][1] == Counter(a).most_common()[1][1] else print(Counter(a).most_common()[0][0])
