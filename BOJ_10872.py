# 팩토리얼 
# 0보다 크거나 같은 N이 주어지면 N!을 출력하기

# 1차 - 메모이제이션을 활용해서 속도를 낮추는 방법을 시도해봄 (효과적인지는 모르겠다)
memo = [1, 1] + [0] * 11
def facto(n):
    if memo[n] != 0:
        return memo[n]
    else:
        return facto(n-1) * n

a = int(input())
print(facto(a))


