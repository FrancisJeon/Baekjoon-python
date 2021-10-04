""" 210820 분해합 항해 40번 """
""" 
N이라는 자연수는 각 자리수의 합과 특정 수를 더해줄 때 N이 된다면 특정 수를 생성자라고 한다.
이 특정 수를 구하고 없을경우 0을 출력시킨다.
"""
import sys
input = sys.stdin.readline

n = int(input())
startingPoint = n - (len(str(n)) * 9)

for i in range(startingPoint, n+1):
    if i < 0:
        continue
    result = (sum(map(int, str(i)))) + i
    if result == n:
        print(i)
        break
else:
    print(0)