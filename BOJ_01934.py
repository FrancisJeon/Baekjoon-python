""" 210617 10:08 항해 25번 QED """
# 테스트 케이스 개수 주어지고
# A, B가 주어지면 둘 사이의 최소공배수 구하기

t = int(input())
for i in range(t):
    a, b = map(int, input().split()) 
    small = a 
    big = b 
    # a < b
    while True:
        r = big % small # 0
        if r == 0:
            # 작은 값이 최대 공약수
            print(int(a/small * b/small) * small)
            break
        big = small
        small = r
