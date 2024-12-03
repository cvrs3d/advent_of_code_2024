import re


def find_mull(data: str) -> list:
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches = re.findall(pattern, data)
    if not matches:
        print("No matches found")
    print(matches[0])
    result = [int(x) * int(y) for x, y in matches]
    return result

def main():
    mull_results_list = []
    memory_segment = ""

    with open("memory_segment.txt", 'r') as memory_file:
        for line in memory_file:
            memory_segment += line.strip()
    memory_file.close()

    mull_results_list = find_mull(memory_segment)
    print(sum(mull_results_list))
    return


if __name__ == "__main__":
    main()
