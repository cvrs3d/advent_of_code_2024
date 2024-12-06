def guard_path(map_lines):
    turns = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }
    delta = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
    }
    num_rows = len(map_lines)
    num_cols = len(map_lines[0])
    visited_positions = set()

    # Initialize the position and direction of the guard
    for y, line in enumerate(map_lines):
        if '^' in line:
            x = line.index('^')
            direction = '^'
            start = (y, x)
            break

    current_pos = start
    visited_positions.add(current_pos)

    # Move the guard
    while True:
        y, x = current_pos
        dy, dx = delta[direction]
        next_pos = (y + dy, x + dx)

        # Check if the guard is still within bounds and not facing an obstacle
        if (0 <= next_pos[0] < num_rows and
                0 <= next_pos[1] < num_cols and
                map_lines[next_pos[0]][next_pos[1]] != '#'):
            # Move forward
            current_pos = next_pos
            visited_positions.add(current_pos)
        else:
            # Turn right
            direction = turns[direction]

        # Break the loop if the guard moves out of bounds
        if not (0 <= next_pos[0] < num_rows and
                0 <= next_pos[1] < num_cols):
            break

    return len(visited_positions)


def main():
    map_lines = []
    with open("input_data.txt", 'r') as input_file:
        for line in input_file:
            map_lines.append(line.strip())
    input_file.close()

    visited_count = guard_path(map_lines)
    print("Number of distinct positions visited:", visited_count)


if __name__ == "__main__":
    main()