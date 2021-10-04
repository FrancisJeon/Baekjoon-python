era = [0, 0] + [1] * 999
for i in range(2, int(1000**0.5)+1):
    if era[i]:
        for j in range(i+i, len(era), i):
            era[j] = 0

n = int(input())
array = list(map(int, input().split()))
ans = 0
for i in array:
    if era[i]: ans += 1
print(ans)