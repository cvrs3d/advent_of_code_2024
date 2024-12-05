def count_x_mas_patterns(matrix):
    n = len(matrix)
    m = len(matrix[0])
    x_mas_patterns = 0

    # Checking 'A' as a center of a struct
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == 'A':
                # Checking / diagonal only
                if ((matrix[i - 1][j - 1] == 'M' and matrix[i + 1][j + 1] == 'S') or
                        (matrix[i - 1][j - 1] == 'S' and matrix[i + 1][j + 1] == 'M')):
                    if ((matrix[i - 1][j + 1] == 'S' and matrix[i + 1][j - 1] == 'M') or
                            (matrix[i - 1][j + 1] == 'M' and matrix[i + 1][j - 1] == 'S')):
                        x_mas_patterns += 1

    return x_mas_patterns


def main():
    matrix = []
    row = []

    with open("puzzle_input.txt", 'r') as puzzle_file:
        for line in puzzle_file:
            row = list(line.strip())
            matrix.append(row)

    puzzle_file.close()

    result = count_x_mas_patterns(matrix)
    print(f"Структура 'X-MAS' появляется {result} раз(а) в головоломке.")


if __name__ == "__main__":
    main()