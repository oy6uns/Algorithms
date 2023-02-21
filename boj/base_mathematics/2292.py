n = int(input())
i = 0
sum = 1

while(1):
    sum += i*6
    i+=1
    if(n<=sum):
        print(i)
        break
