arr = [1, 2, 3, 4]
running_sum = []
total = 0

for num in arr:
    total += num
    running_sum.append(total)

print(running_sum)
