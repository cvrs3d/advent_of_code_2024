def search_word_in_matrix(matrix, word):
    def find_word(line, word):
        joined_line = ''.join(line)
        reversed_word = word[::-1]
        return joined_line.count(word) + joined_line.count(reversed_word)

    def get_column_as_row(matrix, col_index):
        return [row[col_index] for row in matrix]

    def get_diagonals_as_lines(matrix):
        diagonals = []
        n = len(matrix)
        m = len(matrix[0])

        # Диагонали типа /
        for d in range(n + m - 1):
            line = []
            for i in range(max(0, d - m + 1), min(n, d + 1)):
                j = d - i
                line.append(matrix[i][j])
            diagonals.append(line)

        # Диагонали типа \
        for d in range(1 - n, m):
            line = []
            for i in range(max(0, d), min(n, n + d)):
                j = i - d
                line.append(matrix[i][j])
            diagonals.append(line)

        return diagonals

    count = 0

    for row in matrix:
        count += find_word(row, word)

    for col in range(len(matrix[0])):
        column_as_row = get_column_as_row(matrix, col)
        count += find_word(column_as_row, word)

    diagonals = get_diagonals_as_lines(matrix)
    for diagonal in diagonals:
        count += find_word(diagonal, word)

    return count


def main():
    matrix = []
    row = []
    with open("puzzle_input.txt", 'r') as puzzle_file:
        for line in puzzle_file:
            row = list(line.strip())
            matrix.append(row)
    puzzle_file.close()
    word = "XMAS"
    result = search_word_in_matrix(matrix, word)
    print(f"Слово '{word}' встречается {result} раз(а) в головоломке.")


if __name__ == "__main__":
    main()