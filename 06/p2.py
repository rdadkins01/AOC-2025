
import operator


def parse_input(input_list): 
    temp_dict = {"nums": [], "ops": []}
    for line in input_list:
        if line.split()[0].isdigit(): # Cephalapod math sucks...
            temp_dict["nums"].append([x for x in line[::-1]]) # Reverse string, don't split, whitepsace matters
        else:
            temp_dict["ops"] = [x for x in line[::-1]]
    return temp_dict


def calculate(parsed_input):
    operators = {
        "+": operator.add,
        "*": operator.mul,
    }

    temp_list = []
    current_num_list = []
    for op_index, arith_oper in enumerate(parsed_input["ops"]):
        current_num = ""

        for num_list in parsed_input["nums"]:
            current_num = current_num + num_list[op_index]
        current_num_list.append(current_num)

        if arith_oper == "+" or arith_oper == "*":
            current_num_list = [x for x in current_num_list if x.strip()] # Remove emtpy strings
            running_total = 0

            for i in range(0, len(current_num_list) - 1):
                if running_total == 0:
                    running_total = operators[arith_oper](int(current_num_list[i]), int(current_num_list[i+1]))
                else: 
                    running_total = operators[arith_oper](running_total, int(current_num_list[i+1]))

            temp_list.append(running_total)
            current_num_list = []
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
    