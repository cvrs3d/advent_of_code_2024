def parse_map(puzzle_input):
    grid = []
    guard_position = None
    guard_direction = None
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    for y, line in enumerate(puzzle_input.splitlines()):
        grid.append(list(line))
        for x, char in enumerate(line):
            if char in directions:
                guard_position = (x, y)
                guard_direction = char
                grid[y][x] = '.'  # Clear the guard's initial position

    return grid, guard_position, directions[guard_direction]


def turn_right(direction):
    turns = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # ^ > v <
    idx = turns.index(direction)
    return turns[(idx + 1) % 4]


def simulate(grid, start_position, start_direction):
    visited_positions = set()
    visited_positions.add((*start_position, start_direction))  # add direction to the tuple

    x, y = start_position
    direction = start_direction

    while True:
        dx, dy = direction
        next_position = (x + dx, y + dy)

        if 0 <= next_position[0] < len(grid[0]) and 0 <= next_position[1] < len(grid):
            if grid[next_position[1]][next_position[0]] == '#':  # Obstacle ahead
                direction = turn_right(direction)
            else:
                x, y = next_position
                if (x, y, direction) in visited_positions:  # Loop detected
                    break
                visited_positions.add((x, y, direction))
        else:
            break  # Out of bounds

    return visited_positions


def find_loop_positions(grid, guard_position, guard_direction):
    possible_positions = set()

    visited = simulate(grid, guard_position, guard_direction)

    # Теперь учитываем три элемента в каждом кортежи
    for x, y, direction in visited:
        if (x, y) != guard_position and grid[y][x] == '.':
            temp_grid = [row[:] for row in grid]
            temp_grid[y][x] = '#'
            new_visited = simulate(temp_grid, guard_position, guard_direction)

            # If new simulation has a loop, include this position
            if len(new_visited) < len(visited):
                possible_positions.add((x, y))

    return possible_positions


# Пример тестирования
puzzle_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

grid, guard_position, guard_direction = parse_map(puzzle_input)
loop_positions = find_loop_positions(grid, guard_position, guard_direction)
print(len(loop_positions))