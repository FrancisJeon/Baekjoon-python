# Binary numbers 210924
# 주어진 양수 n의 이진수 1의 위치를 전부 반환하기
# 첫 줄에는 갯수, 둘째 줄에는 갯수에 맞는 숫자들이 입력되는듯
# 1차
# bin() 함수로 이진수로 변경시킨 다음 [2:] 스플릿 후 1의 위치 찾기
        
# 숫자 형태로 문제가 발생하는것 같아서 최대한 문제에 맞추기 위한 코드 짜기로 -> input 순서를 잘못잡았다.

for _ in range(int(input())):
    i = int(input())
    bin_val = list(bin(i)[2:][::-1])
    ans = [str(i) for i, j in enumerate(bin_val) if j == '1']
    print(' '.join(ans))

