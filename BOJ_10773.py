""" 210618 12:30 항해 23번 QED 제로"""
import sys
k = int(sys.stdin.readline())
money = []
sum = 0
def pushMoney(inp):
    money.append(inp)

def popMoney():
    if len(money) != 0:
        del money[-1]

def countSum():
    for i in money:
        global sum 
        sum += i

for _ in range(k):
    k = int(sys.stdin.readline())
    if k == 0:
        popMoney()
    else:
        pushMoney(k)

countSum()

print(sum)