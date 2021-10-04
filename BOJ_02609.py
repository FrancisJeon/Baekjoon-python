""" 210616 21:12 항해 16번 QED """
a, b = map(int, input().split())
num1 = max(a,b)
num2 = min(a,b)
while True:
    r = num1 % num2
    if r == 0:
        print(num2) # 최대공약수
        lcm = int(a*b/num2)
        print(lcm)
        break
    num1 = num2
    num2 = r
