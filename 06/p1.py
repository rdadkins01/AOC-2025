
import operator


def parse_input(input_list):
    temp_dict = {"nums": [], "ops": []}
    for line in input_list:
        if line.split()[0].isdigit():
            temp_dict["nums"].append([x for x in line.split()])
        else:
            temp_dict["ops"] = [x for x in line.split()]
    return temp_dict


def calculate(parsed_input):
    operators = {
        "+": operator.add,
        "*": operator.mul,
    }

    temp_list = []
    for index, arith_oper in enumerate(parsed_input["ops"]):
        running_total = 0
        for i in range(0, len(parsed_input["nums"]) - 1):
            if running_total == 0:
                running_total = operators[arith_oper](int(parsed_input["nums"][i][index]), int(parsed_input["nums"][i+1][index]))
            else:
                running_total = operators[arith_oper](running_total, int(parsed_input["nums"][i+1][index]))

        temp_list.append(running_total)
    return temp_list


def main():
    input_file = "puzzle_input.txt"

    with open(input_file, "r") as file:
        puzzle_input = file.read().splitlines()

    parsed_input = parse_input(puzzle_input)
    calculated_items = calculate(parsed_input)

    total = 0
    for value in calculated_items:
        total += value

    print(total)


if __name__ == "__main__":
    main()
    