# https://www.acmicpc.net/problem/14719
# 고인 빗물의 양을 확인

h, w = map(int, input().split())
block = list(map(int, input().split()))
rain = 0

for i in range(1, w-1):
    max_left = max(block[:i])
    max_right = max(block[i+1:])

    compare = min(max_left, max_right)

    if block[i] < compare:
        rain += compare - block[i]
print(rain)