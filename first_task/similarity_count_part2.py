similarity_score = []

# We calculate how many of each number in left list is present in the right list
# Then we multiply left list number by this count
# Then we append the result to the similarity_score
# Then we do sum(similarity_score)
# We got the result???

left_numbers_list = []
right_numbers_list = []

def count_appearances(number):
    return right_numbers_list.count(number)

def main():

    with open("list.txt", 'r') as list_file:
        for line in list_file:
            number1, number2 = map(int, line.split())
            left_numbers_list.append(number1)
            right_numbers_list.append(number2)

    list_file.close()
    for number in left_numbers_list:
        similarity_score.append(number * count_appearances(number))

    print(sum(similarity_score))
    print(19097157 < 2113135)
    return


if __name__ == "__main__":
    main()

