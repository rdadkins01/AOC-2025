
input_file = "puzzle_input.txt"


def main():

    with open(input_file, "r") as file:
        puzzle_input = file.read().splitlines()

    pos_zero_qty = 0
    current_position = 50

    for turn in puzzle_input:
        if int(turn[1:]) > 100: 
            turn_qty = int(turn[-2:])
            pos_zero_qty += int(turn[1])
        else:
            turn_qty = int(turn[1:])

        if turn[0] == 'L':
            prohibit_zero_count = False
            if current_position == 0:
                prohibit_zero_count = True
            current_position -= turn_qty
            if current_position < 0:
                current_position += 100
                if not prohibit_zero_count:
                    pos_zero_qty += 1
            elif current_position == 0: pos_zero_qty += 1

        else:
            current_position += turn_qty
            if current_position > 99:
                current_position -= 100
                pos_zero_qty += 1
            elif current_position == 0: pos_zero_qty += 1

    print(f"Current position: {current_position}, Zero Quantity: {pos_zero_qty}")


if __name__ == "__main__":
    main()
    