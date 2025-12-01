
input_file = "test_input.txt"

def main():

    with open(input_file, "r") as file:
        puzzle_input = file.read().splitlines()

    print(puzzle_input)


if __name__ == "__main__":
    main()