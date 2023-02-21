matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result_matrix = []

for i in range(len(matrix1)):
    row = []
    for el in range(len(matrix1[i])):
        result = matrix1[i][el] * matrix2[i][el]
        row.append(result)
    result_matrix.append(row)

print(result_matrix)