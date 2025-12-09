

def main():
    input_file = "puzzle_input.txt"

    with open(input_file, "r") as file:
        puzzle_input = []
        for line in file.read().splitlines():
            puzzle_input.append([x for x in line])

    beam_positions = [puzzle_input[0].index("S")]
    split_count = 0
    for line in puzzle_input[1:]:
        new_beam_positions = []
        empty_line = True
        non_split_beams = []
        for beam_pos in beam_positions:

            if line[beam_pos] == "^": # Split
                empty_line = False
                if beam_pos + 1 not in new_beam_positions:
                    new_beam_positions.append(beam_pos + 1)
                if beam_pos - 1 not in new_beam_positions:
                    new_beam_positions.append(beam_pos - 1)
                split_count += 1
            else: # Don't split, but keep beam
                non_split_beams.append(beam_pos)

        if not empty_line: 
            beam_positions = new_beam_positions # Set next beam positions
            for beam in non_split_beams:
                if beam not in beam_positions:
                    beam_positions.append(beam) # Include beams that didn't split

    print(f'Beam Positions: {beam_positions}')
    print(f'Split Count: {split_count}')


if __name__ == "__main__":
    main()
    