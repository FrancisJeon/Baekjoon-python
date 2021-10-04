# 별 찍기7 210915
""" 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
n = int(input())
for i in range(1, n):
    answer = ' ' * (n - i) + ('*' * (i * 2 - 1))
    print(answer)

for i in range(n, 0, -1):
    answer = ' ' * (n - i) + ('*' * (i * 2 - 1))
    print(answer)
