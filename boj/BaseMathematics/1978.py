n = int(input())
arr = list(map(int, input().split()))
demi = arr.copy()
sum = 0

for i in range(n):
    if arr[i] == 1:
            demi[i] = 0
    else:
         for j in range(2, arr[i]):
            if demi[i]%j == 0:
                demi[i] = 0

for j in range(n):
    if demi[j] != 0:
         sum += 1

print(sum)