def process_matrix_17(matrix):
    n = len(matrix)
    off_diag_elements = []
    # Собираем все внедиагональные элементы
    for i in range(n):
        for j in range(n):
            if i != j:
                off_diag_elements.append(matrix[i][j])
    # Среднее значение внедиагональных элементов
    avg_off_diag = sum(off_diag_elements) / len(off_diag_elements)
    # Обрабатываем столбцы
    for j in range(n):
        if j % 2 == 1:  # нечётный столбец
            for i in range(n):
                matrix[i][j] /= avg_off_diag
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
result = process_matrix_17(matrix)
print("\nРезультат:")
for row in result:
    print([f"{x:.2f}" for x in row])
