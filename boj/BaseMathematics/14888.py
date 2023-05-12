# https://www.acmicpc.net/problem/14888

import sys
from itertools import permutations
from collections import deque

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
operator_num = list(map(int, sys.stdin.readline().split()))

# 연산자 종류
operator_type = ['+', '-', '*', '//']

# 연산자 문자로 저장할 배열 선언
operator = []

# 빈 배열에 입력받은 연산자 추가하기
for i in range(4):
    if operator_num[i] == 0:
        pass
    else:
        for j in range(operator_num[i]):
            operator.append(operator_type[i])

# 만들수 있는 연산자 배열의 경우의 수 - 순열 사용
operator_case = list(permutations(operator, len(operator)))

# 배열에 저장되어 있는 배열의 경우의 수를 deque에 저장
q = deque(operator_case)

# 최댓값, 최솟값 초기화
max_result = -1e9
min_result = 1e9

while q:
    each_case = q.popleft()
    result = data[0]
    # 연산 수행
    for i in range(1, len(data)):
        if each_case[i-1] == '+':
            result += data[i]
        elif each_case[i-1] == '-':
            result -= data[i]
        elif each_case[i-1] == '*':
            result *= data[i]
        else:
            if result < 0:
                result = -(abs(result) // data[i])
            else:
                result //= data[i]
    # 최댓값, 최솟값 업데이트
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)