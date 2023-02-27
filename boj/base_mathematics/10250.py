import math

x = int(input())
for _ in range(x):
    h, w, n = map(int, input().split())
    floor = n % h
    if floor == 0:
        floor = h
    num = math.ceil(n / h)
    #zfill('인자') : 문자열의 길이보다 전달된 숫자보다 작을 때 앞 부분을 0으로 채움 
    print(int(str(floor) + str(num).zfill(2)))