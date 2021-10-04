# 소수 210928
""" 
M과 N이 각 줄에 입력되면 M이상 N 이하의 자연수 중 소수인 것을 골라 소수의 합, 최솟값 찾기 
소수가 없다면 -1 출력
"""
l = [int(input()) for _ in range(2)]
m, n = l[0], l[1]

sieve = [0, 0] + [1] * 10001

for i in range(2, int(len(sieve)**0.5)):
    if sieve[i]:
        for j in range(i+i, len(sieve), i):
            sieve[j] = 0

primes = []
for i in range(m, n+1):
    if sieve[i]:
        primes.append(i)

print(sum(primes), primes[0], sep="\n") if primes else print(-1)

# 괜찮은 정답코드
# a는 에라토스테네스, b는 소수를 담은 리스트
# c에 set로 범위를 담아준 뒤 b를 기준으로 교집합 부분만 사용
n, a, b = 10000, [0, 0]+[1]*9999, []
for i in range(2, n+1):
  if a[i]:
    b.append(i)
    for j in range(2*i, n+1, i):
        a[j] = 0
M, N = int(input()), int(input())
c = set(list(range(M, N+1)))
d = set(b) & c
if d:
    print(sum(d), min(d))
else:
    print(-1)
