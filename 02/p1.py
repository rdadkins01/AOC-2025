
input_file = "puzzle_input.txt"


def duplicate_check(value):
    if value[0:int(len(value)/2)] == value[int(len(value)/2):]:
        return True
    return False


def main():
    with open(input_file, "r") as file:
        puzzle_input = file.read().split(',')

    invalid_ids = []
    for item in puzzle_input:
        for id in range(int(item.split('-')[0]), int(item.split('-')[1]) + 1):
            if len(str(id)) % 2 == 0:
                if duplicate_check(str(id)):
                    invalid_ids.append(id)

    id_total = 0
    for id in invalid_ids:
        id_total += id

    print(f"Invalid ID total: {id_total}")


if __name__ == "__main__":
    main()