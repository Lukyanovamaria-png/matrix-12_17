def process_matrix_12(matrix):
    n = len(matrix)
    # Сумма диагональных элементов
    diag_sum = sum(matrix[i][i] for i in range(n))
    # Среднее значение диагональных элементов
    avg_diag = diag_sum / n
    # Обрабатываем столбцы
    for j in range(n):  # j — номер столбца
        if j % 2 == 1:  # нечётный столбец (индексация с 0)
            for i in range(n):
                matrix[i][j] /= avg_diag
    return matrix
# Пример использования
n = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
result = process_matrix_12(matrix)
print("\nРезультат:")
for row in result:
    print([f"{x:.2f}" for x in row])
