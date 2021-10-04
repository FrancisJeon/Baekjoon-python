# 피보나치 수 5 210927
# 메모이제이션
memo = [0, 1, 1] + [False] * 20
def fibo(n):
    if n <= 2: return memo[n]
    if memo[n]: return memo[n]
    else: return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))
