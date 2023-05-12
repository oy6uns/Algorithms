height = []

for _ in range(9):
    height.append(int(input()))

sum_arr = sum(height)
dif = sum_arr - 100
height.sort()

for i in range(9):
    for j in range(i+1, 9):
        if height[i] + height[j] == dif:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    print(height[k])
            exit()