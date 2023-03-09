a, b = map(int, input().split())
prod = a * b

while(1):
    if a > b:
        a = a - b
    elif b > a:
        b = b - a
    else:
        print(a)
        break

print(prod//a)
