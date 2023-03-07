N = int(input())

num = list(map(int, input().split()))
min = num[0]
max = num[0]

for i in num[1:]:
    if(i<min):
           min = i
    if(i>max):
           max = i
print(min, max)