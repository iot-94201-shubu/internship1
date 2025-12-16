data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))
result = []

for i in range(len(data[0])):   # number of columns
    column_sum = 0
    for row in data:
        column_sum += row[i]
    result.append(column_sum / len(data))

print(result)
