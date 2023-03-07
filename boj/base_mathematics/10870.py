n = int(input())

def fib(n):
    a = 0
    b = 1   
    for _ in range(n):
        if(a==min(a, b)):
            a = a+b
        else:
            b = a+b
    print(min(a, b))

fib(n)