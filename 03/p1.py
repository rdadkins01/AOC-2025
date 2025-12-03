

def main():
    input_file = "puzzle_input.txt"

    with open(input_file, "r") as file:
        puzzle_input = file.read().splitlines()

    joltage_list = []
    for battery_bank in puzzle_input:
        largest_batteries = '00'
        batteries = [int(x) for x in battery_bank]
        for battery in batteries:
            if int(largest_batteries[1] + str(battery)) > int(largest_batteries):
                largest_batteries = largest_batteries[1] + str(battery)

            elif int(battery) > int(largest_batteries[1]):
                largest_batteries = largest_batteries[0] + str(battery)

        joltage_list.append(largest_batteries)

    joltage_total = 0
    for joltage in joltage_list:
        joltage_total += int(joltage)

    print(f"MAXIMUM JOLTAGE: {joltage_total}")


if __name__ == "__main__":
    main()
