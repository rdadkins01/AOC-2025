

def roll_check(y_index, x_index, puzzle_input):
    if (x_index >= len(puzzle_input[0]) or # Out of bounds check
        x_index < 0 or
        y_index >=len(puzzle_input) or
        y_index < 0):
        return 0
    
    if puzzle_input[y_index][x_index] == "@":
        return 1
    return 0


def roll_accessible(y_index, x_index, puzzle_input):
    roll_obstruction_count = 0
    roll_obstruction_count += roll_check(y_index -1, x_index -1, puzzle_input) #top left
    roll_obstruction_count += roll_check(y_index -1, x_index, puzzle_input) # top center
    roll_obstruction_count += roll_check(y_index -1, x_index + 1, puzzle_input) # top right
    roll_obstruction_count += roll_check(y_index, x_index - 1, puzzle_input) # middle left
    roll_obstruction_count += roll_check(y_index, x_index + 1, puzzle_input) # middle right
    roll_obstruction_count += roll_check(y_index + 1, x_index - 1, puzzle_input) # bottom left
    roll_obstruction_count += roll_check(y_index + 1, x_index, puzzle_input) # bottom center
    roll_obstruction_count += roll_check(y_index + 1, x_index + 1, puzzle_input) # bottom right
    if roll_obstruction_count < 4:
        return True
    return False


def rolls_to_be_removed(puzzle_input):
    temp_list = []
    for y_index, line in enumerate(puzzle_input):
        for x_index, position in enumerate(line):
            if position == "@" and roll_accessible(y_index, x_index, puzzle_input):
                temp_list.append((y_index, x_index))
    return temp_list


def remove_rolls(grid, accessible_rolls):
    for roll in accessible_rolls:
        grid[roll[0]][roll[1]] = "x"
    return grid


def main():
    input_file = "puzzle_input.txt"

    with open(input_file, "r") as file:
        puzzle_input = []
        for line in file.read().splitlines():
            puzzle_input.append([x for x in line])

    rolls_removed = True
    total_rolls_removed = 0
    while rolls_removed:
        accessible_rolls = rolls_to_be_removed(puzzle_input)
        puzzle_input = remove_rolls(puzzle_input, accessible_rolls)
        if len(accessible_rolls) > 0:
            total_rolls_removed += len(accessible_rolls)
            rolls_removed = True
        else:
            rolls_removed = False

    print(f"{total_rolls_removed} rolls of paper are accessible.")


if __name__ == "__main__":
    main()
    