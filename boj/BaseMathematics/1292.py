arr = []
num = 1
sum = 0

while len(arr)<1000:
    for _ in range(num):
        arr.append(num)
    num += 1

start, end = map(int, input().split())
for i in range(start-1, end):
    sum += arr[i]

print(sum)