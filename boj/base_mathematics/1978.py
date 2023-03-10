n = int(input())
arr = list(map(int, input().split()))
demi = []

for i in range(n):
    for j in range(2, arr[i]+1):
        if arr[i]%j == 0:
            demi.append(arr[i])
print(len(demi))