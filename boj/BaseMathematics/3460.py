t = int(input())
count = 0
check = []

for i in range(t):
    n = int(input())
    while(n!=0): 
        if(2**count<=n):
            count += 1
        else:
            check.insert(0, count-1)
            n = n - 2**(count-1)
            count = 0
    for j in range(len(check)):
        print(check[j], end=" ")
    # print('\n')
    count = 0
    check = []
            
    
