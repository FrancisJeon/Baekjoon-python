# 괄호의 값
""" 
(), []를 이용해서 만든 괄호가 주어지는데 올바른 괄호가 아니면 0이 출력된다.
()는 2점, []는 3점인데 괄호 안에 괄호가 있다면 다시 곱을 해준다.
(x)는 2*x로 계산되고 [x]는 3*x 점으로 계산된다
(()[[]])([]) 
(2+3*3)*2 + 2*3 > 22 + 6 > 28점
괄호가 시작될 때 해당 괄호가 끝날 때 까지의 모든 괄호를 한곳에 담아준다. 이 괄호는 하나의 점수를 나타낸다.

* 올바른 괄호인지 검사 -> 
1. (와 [를 카운팅 하다가 -가 되면 return False, 반복문을 다 돌고 카운팅이 전부 0이면 True
괄호가 한 종류라면 정상적으로 판단할 수 있지만 ([)] 같은 형태의 괄호는 정상적으로 판단하지 못한다. -> 이를 보완하기 위해서 '[)'와 '(]'가 존재한다면 False를 리턴하도록 해보았다. 최종적으로 알고리즘은 2번 방식으로 만들었다.
    # if '(]' in parenthesis or '[)' in parenthesis:
    #     return False
2. 스택을 처음부터 끝까지 활용하고 counting을 사용하지 않는 방법
스택에 (와 [는 담고 )와 ]를 만나면 stack의 top이 맞는 쌍이 아니라면 False, 모든 괄호를 다 살핀 뒤 stack이 비어있으면 True


* 알고리즘 - 가장 작은 단위의 괄호들을 숫자로 변경, +를 붙인다.
(2+[3+])(3+)
만약 숫자가 [] 또는 ()로 둘러쌓여 있다면 0을 더한 뒤 곱을 해준다
예) [x]는 x 곱하기 3으로 바꾸기
(2+9)6+
괄호 내부의 값이 연산이 가능한 상태라면 연산을 해준다.
(11)6+
위를 반복해주면 22+6+
* 알고리즘 2 - (와 [를 스택에 쌓다가 )나 ]를 만나면 스택에서 빼서 숫자로 바꿔준다
(2[3] # 만약 ]를 뺄 때 안에 숫자가 있다면 곱하기 3
(2,9) # )를 만나서 *2를 하려고 하는데 내부의 숫자들은 전부 더해주자 
22,6-> 28
"""
# 1차
def is_right(parenthesis):
    s = []
    for i in range(len(parenthesis)):
        if parenthesis[i] == '(' or parenthesis[i] == '[':
            s.append(parenthesis[i])
        elif parenthesis[i] == ')':
            if not s or s[-1] != '(':
                return False
            s.pop()
        elif parenthesis[i] == ']':
            if not s or s[-1] != '[':
                return False
            s.pop()
    return True if not s else False


parenthesis = input()
if is_right(parenthesis):
    s = [] 
    for i in parenthesis: # 카운팅 시작
        score = 0
        if i == '(' or i == '[':
            s.append(i)
        elif i == ')':
            a = s.pop() # 출력된 문자 또는 숫자를 확인한다.
            if a != '(':
                while a != '(':
                    score += a  # 2
                    a = s.pop()
                score *= 2
                s.append(score)
            elif a == '(':
                s.append(2)
        elif i == ']':
            a = s.pop()
            if a != '[':
                while a != '[':
                    score += a
                    a = s.pop()
                score *= 3
                s.append(score)
            elif a == '[':
                s.append(3)
    print(sum(s))
else:
    print(0)

# 2번, 정답코드 복사해옴
s = input()
def is_check(s):    # 올바른 괄호열인지 확인하는 함수
    stack = []
    flag = True
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        else:    # ) ]
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
            else:    # ]
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
    if not stack and flag:
        return True
    return False


def calc_value(s):    # 괄호의 값을 계산하는 함수
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        else:    # ) ]
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:    # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '(':
                            stack[-1] = temp * 2
                            break
                        else:    # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()
            else:    # ]
                if stack[-1] == '[':
                    stack[-1] = 3
                else:    # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '[':
                            stack[-1] = temp * 3
                            break
                        else:    # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()
    return sum(stack)


if is_check(s):
    print(calc_value(s))
else:
    print(0)
