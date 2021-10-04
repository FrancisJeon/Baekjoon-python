# N번째 큰 수 210927
""" 
첫줄 P 입력 (입력 갯수)
그 뒤로 입력하는 값들은 10개의 숫자들
출력값은 3번째로 큰 수
"""
# 132ms
arrs = [ sorted(list(map(int, input().split()))) for _ in range(int(input())) ]
for i in arrs:
    print(i[-3])