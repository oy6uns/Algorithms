start = int(input())
end = int(input())
prime = []
count = 0

for n in range(start, end+1):
    count = 0
    if n == 1:
        continue
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count == 0:
        prime.append(n)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])