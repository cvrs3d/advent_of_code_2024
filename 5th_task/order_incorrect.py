from print_queue import parse_file, is_update_correct, find_middle_page

def reorder_update(order_rules, update):
    """
    Correctly orders an update based on the order_rules.
    """
    ordered_update = []
    remaining_items = update[:]

    while remaining_items:
        # ищем элемент, который можно поставить в ordered_update
        for item in remaining_items:
            if all((item, other) not in order_rules for other in remaining_items if other != item):
                ordered_update.append(item)
                remaining_items.remove(item)
                break
    return ordered_update

def process_and_reorder_updates(order_rules, updates):
    middle_sum = 0
    for update in updates:
        if not is_update_correct(order_rules, update):
            corrected_update = reorder_update(
                order_rules,
                update
            )
            print(corrected_update)
            middle_sum += find_middle_page(corrected_update)
    return middle_sum

def main():
    file_name = "input_data.txt"
    order_rules, updates = parse_file(file_name)
    sum_middle_pages = process_and_reorder_updates(order_rules, updates)
    print("Сумма средних страниц для некорректно упорядоченных обновлений:", sum_middle_pages)
    return

if __name__ == "__main__":
    main()