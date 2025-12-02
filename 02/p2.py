import math


def get_values_to_check(value):
    current_num = ""
    values_to_check = []
    for num in value:

        # Dont need to check values longer than half the length of original value
        if len(current_num) <= int(math.floor(len(value)/2)):

            # Also don't need to add values that can't completely repeat due to length
            if current_num != "":
                if len(value) % len(current_num) == 0:
                    values_to_check.append(current_num)
            current_num += num
    return values_to_check


def duplicate_check(value):
    values_to_check = get_values_to_check(value)
    for questionable_id in values_to_check:
        mismatch = False

        qty_to_check = int(len(value) / len(questionable_id))

        for multiplier in range(1, qty_to_check + 1):
            end_pos = (len(questionable_id) * multiplier)
            start_pos = end_pos - len(questionable_id)
            if questionable_id != value[start_pos:end_pos]: 
                mismatch = True

        if not mismatch:
            return True
    return False


def main():
    input_file = "puzzle_input.txt"
    with open(input_file, "r") as file:
        puzzle_input = file.read().split(',')

    invalid_ids = []
    for item in puzzle_input:
        for id in range(int(item.split('-')[0]), int(item.split('-')[1]) + 1):
            if duplicate_check(str(id)):
                invalid_ids.append(id)

    id_total = 0
    for id in invalid_ids:
        id_total += id

    print(f"Invalid IDs: {invalid_ids}")
    print(f"Invalid ID total: {id_total}")


if __name__ == "__main__":
    main()
    