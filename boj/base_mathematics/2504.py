import sys

bracket = sys.stdin.readline().strip()
# 현재 곱셈값을 임시로 저장하기 위한 변수
tmp = 1
# 출력할 결과값을 저장하는 변수
res = 0
stack = []

for i in range(len(bracket)):
    b = bracket[i]
    if b == '(':
        tmp *= 2
        stack.append(b)
    elif b == '[':
        tmp *= 3
        stack.append(b)
    elif b == ')':
        # stack이 비어있거나, stack의 최상단 값이 '['라면 짝이 안 맞기에
        if not stack or stack[-1] == '[':
            res = 0
            break
        if bracket[i-1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if bracket[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop()

if stack:
    res = 0
print(res)


        
