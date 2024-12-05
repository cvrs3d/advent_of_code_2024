def is_update_correct(order_rules, update):
    """Проверяет, находится ли обновление в правильном порядке."""
    for x, y in order_rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def find_middle_page(update):
    """Находит среднюю страницу (в случае нечетного количества страниц)."""
    mid_index = len(update) // 2
    return update[mid_index]


def process_updates(order_rules, updates):
    """Обрабатывает список обновлений и возвращает сумму средних страниц для корректных обновлений."""
    middle_sum = 0
    incorrect_updates = []
    for update in updates:
        if is_update_correct(order_rules, update):
            middle_sum += find_middle_page(update)
        else:
            incorrect_updates.append(update)
    print("Incorrect updates: ", incorrect_updates, "\n")
    return middle_sum


def parse_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

    sections = content.strip().split('\n\n')
    if len(sections) != 2:
        raise ValueError("File format is incorrect. Expecting exactly two sections.")

    raw_rules, raw_updates = sections

    order_rules = []
    for line in raw_rules.splitlines():
        if not line.strip():
            continue
        x, y = map(int, line.strip().split("|"))
        order_rules.append((x, y))

    updates = []
    for line in raw_updates.splitlines():
        if not line.strip():
            continue
        update = list(map(int, line.strip().split(",")))
        updates.append(update)

    return order_rules, updates

def main():
    file_name = "input_data.txt"
    order_rules, updates = parse_file(file_name)

    print("Правила порядка:")
    for rule in order_rules:
        print(rule)

    print("\nОбновления:")
    for update in updates:
        print(update)

    sum = process_updates(
        order_rules,
        updates)

    print("\nMiddle digit sum = ", sum, "\n")
    return



if __name__ == "__main__":
    main()