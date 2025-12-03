
def shift_check(largest_batteries):
    increase_found = False
    index = 0
    for index, item in enumerate(largest_batteries):
        if not increase_found:
            if index > 0 and item > largest_batteries[index - 1]:
                increase_found = True
                return increase_found, index
    return increase_found, index


def shift_batteries(battery_list, index_start):
    for new_index in range(index_start, 12):
        battery_list[new_index - 1] = battery_list[new_index]
    return battery_list
     

def main():
    input_file = "puzzle_input.txt"

    with open(input_file, "r") as file:
        puzzle_input = file.read().splitlines()

    joltage_list = []
    for battery_bank in puzzle_input:
        batteries = [int(x) for x in battery_bank]

        # Largest batteries are initially the first 12 nums
        largest_batteries = [x for x in batteries[:12]]
        for battery in batteries[12:]:
            increase_found, shift_index = shift_check(largest_batteries)

            if increase_found:
                largest_batteries = shift_batteries(largest_batteries, shift_index)
                largest_batteries[11] = battery
            else:
                if int(battery) > int(largest_batteries[11]):
                    largest_batteries[11] = battery

        joltage_list.append(largest_batteries)

    joltage_total = 0
    for joltage in joltage_list:
        joltage_total += int("".join(map(str, joltage)))

    print(f"MAXIMUM JOLTAGE: {joltage_total}")


if __name__ == "__main__":
    main()
