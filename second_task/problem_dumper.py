
from find_safe_reports import is_safely_decreasing, is_safely_increasing


def problem_dumper(levels: list[int], tolerate: int) -> list:

    if is_safely_decreasing(levels) or is_safely_increasing(levels):
        return levels

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safely_decreasing(modified_levels) or is_safely_increasing(modified_levels):
            return modified_levels

    return []






def main():
    reports = []
    with open("reports.txt", 'r') as data_file:
        for line in data_file:
            reports.append(list(map(int, line.split())))
    data_file.close()

    safe_reports = []

    for report in reports:
        safe_version = problem_dumper(report, 3)
        if safe_version:
            safe_reports.append(safe_version)

    print(f'Safe reports count: {len(safe_reports)}')
    return

if __name__ == "__main__":
    main()
