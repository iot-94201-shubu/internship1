matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)
def matrix_add_sub(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    addition = []
    subtraction = []

    for i in range(rows):
        add_row = []
        sub_row = []
        for j in range(cols):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        addition.append(add_row)
        subtraction.append(sub_row)

    return addition, subtraction
add_result, sub_result = matrix_add_sub(matrix_list, matrix_tuple)

print("Addition Result Matrix:")
for row in add_result:
    print(row)

print("\nSubtraction Result Matrix:")
for row in sub_result:
    print(row)
