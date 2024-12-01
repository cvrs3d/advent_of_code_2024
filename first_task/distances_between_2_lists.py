def absolute_distance(left_num, right_num):
    return abs(left_num - right_num)


def main():
    left_numbers_list = []
    right_numbers_list = []

    with open("list.txt", 'r') as list_file:
        for line in list_file:
            number1, number2 = map(int, line.split())
            left_numbers_list.append(number1)
            right_numbers_list.append(number2)

    list_file.close()
    left_numbers_list.sort()
    right_numbers_list.sort()
    print(
        f"Left numbers list: {left_numbers_list}\nRight numbers list: {right_numbers_list}")

    distances_list = []

    for i, left in enumerate(left_numbers_list):
        print(f"{left} - {right_numbers_list[i]} = {absolute_distance(left, right_numbers_list[i])}\n")
        distances_list.append(absolute_distance(left, right_numbers_list[i]))

    print(sum(distances_list))

if __name__ == "__main__":
    main()
