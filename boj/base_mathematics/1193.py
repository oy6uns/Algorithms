x = int(input())

sum = 2
index = 1
row_index = 0

while(1):
    if x<=index:
        row_index = index - x
        if sum % 2 == 1:
            print(str(sum-row_index-1)+ '/' +str(row_index+1))
            break
        else:
            print(str(row_index+1)+ '/' +str(sum-row_index-1))
            break
    index += sum
    sum += 1
