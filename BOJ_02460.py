# 지능형 기차 210927
""" 
10개의 역이 있는데 1번역에서 출발하여 10번역에서 전원 하차한다.
출발부터 종점까지 가는 중 기차 안에 가장 사람이 많은 구간에 사람수를 출력
n, k = 내린 사람, 탄 사람
10번 입력
"""
M = 0
cur = 0
for _ in range(10):
    o, i = map(int, input().split()) 
    # out, in
    cur += i - o
    # 최대값 변경하는 방법 
    # if M < cur: M = cur
    M = max(cur, M)
print(M)
