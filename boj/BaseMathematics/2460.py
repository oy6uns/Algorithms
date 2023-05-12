arr = [list(map(int, input().split())) for _ in range(10)]
count = 0
comp = 0

for i in range(10):
    count = count - arr[i][0] + arr[i][1]
    if comp < count:
        comp = count
print(comp)