

def is_safely_increasing(levels: list) -> bool:
    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return False
        if levels[i] > levels[i + 1]:
            return False
        if abs(levels[i] - levels[i + 1]) > 3:
            return False
    return True


def is_safely_decreasing(levels: list) -> bool:
    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return False
        if levels[i] < levels[i + 1]:
            return False
        if abs(levels[i] - levels[i + 1]) > 3:
            return False
    return True

def is_safe(levels: list) -> bool:
    for i, level in enumerate(levels):
        if level == levels[i+1]:
            return False
        if level > levels[i+1]:
            return is_safely_decreasing(levels)
        if level < levels[i+1]:
            return is_safely_increasing(levels)
    return True

def main():
    safe_reports_count = 0

    with open("reports.txt", 'r') as data_file:
        for line in data_file:
            level_line = list(map(int, line.split()))
            if is_safe(level_line):
                safe_reports_count += 1

    print(safe_reports_count)
    data_file.close()
    return


if __name__ == "__main__":
    main()