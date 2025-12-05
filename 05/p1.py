

def main():
    input_file = "puzzle_input.txt"

    with open(input_file, "r") as file:
        fresh_ingredient_ranges = []
        ingredient_ids = []
        for line in file.read().splitlines():
            if "-" in line:
                fresh_ingredient_ranges.append(line)
            else:
                if line != "":
                    ingredient_ids.append(line)

    good_ingredients = set()
    for ingredient in ingredient_ids:
        match  = False
        for ingredient_range in fresh_ingredient_ranges:
            if not match:
                if int(ingredient) in range(int(ingredient_range.split("-")[0]), int(ingredient_range.split("-")[1]) + 1):
                    match = True
                    good_ingredients.add(ingredient)

    print(f"There are {len(good_ingredients)} available fresh ingredient IDs!")


if __name__ == "__main__":
    main()
    