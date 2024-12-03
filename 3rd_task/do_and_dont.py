import re

def parse_data(data: str) -> list:
    pattern = r"(do\(\)|don't\(\)|mul\((\d+),\s*(\d+)\))"
    matches = re.findall(pattern, data)
    print(matches)
    return matches

def find_muls(parsed_data: list) -> list:
    enabled = True
    results = []

    for match in parsed_data:
        command = match[0]
        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        elif "mul" in command and enabled:
            x, y = int(match[1]), int(match[2])
            results.append(x * y)
    return results

def main():
    with open("memory_segment.txt", 'r') as memory_file:
        data = memory_file.read()
    memory_file.close()
    parsed_data = parse_data(data)
    muls_results = find_muls(parsed_data)
    print(sum(muls_results))
    return

if __name__ == "__main__":
    main()