def get_matrix(n, m, value):
    matrix =[]
    for n in range(len(matrix)):
        matrix.append([])
        for m in range(len(matrix)):
            matrix.append(value )
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

