

def get_good_ingredients(fresh_ingredient_ranges):
    temp_list = []
    for ingredient_range in fresh_ingredient_ranges:
        ingredient_range_start = int(ingredient_range.split("-")[0])
        ingredient_range_end = int(ingredient_range.split("-")[1])
        if len(temp_list) == 0:
            temp_list.append(ingredient_range)
        else:
            for index, good_range in enumerate(temp_list):
                good_range_start = int(good_range.split("-")[0])
                good_range_end = int(good_range.split("-")[1])

                if ingredient_range_start >= good_range_start and ingredient_range_start <= good_range_end:
                    ingredient_range_start = int(good_range_end) + 1
                if ingredient_range_end >= good_range_start and ingredient_range_end <= good_range_end:
                    ingredient_range_end = int(good_range_start) - 1

                if ingredient_range_start <= good_range_start and ingredient_range_end >= good_range_end:
                    if ingredient_range not in temp_list:
                        # Current range envelopes existing range, current range not in list, replace existing range
                        temp_list[index] = f"{ingredient_range_start}-{ingredient_range_end}"
                    else:
                        # Current range envelopes existing range, current range already in list, remove existing range
                        temp_list.remove(good_range)

            if ingredient_range_end >= ingredient_range_start:
                temp_list.append(f"{ingredient_range_start}-{ingredient_range_end}")
    return temp_list


def sum_ingredients(good_ingredients):
    total = 0
    for ing_range in good_ingredients:
        total += (int(ing_range.split("-")[1]) - int(ing_range.split("-")[0])) + 1
    return total


def main():
    input_file = "puzzle_input.txt"

    with open(input_file, "r") as file:
        fresh_ingredient_ranges = []
        for line in file.read().splitlines():
            if "-" in line:
                fresh_ingredient_ranges.append(line)

    good_ingredients = get_good_ingredients(fresh_ingredient_ranges)
    last_run_list = []
    while last_run_list != good_ingredients: 
        last_run_list = good_ingredients
        good_ingredients = get_good_ingredients(last_run_list)

    total_good_ingredients = sum_ingredients(good_ingredients)
    print(f"There are {total_good_ingredients} available fresh ingredient IDs!")


if __name__ == "__main__":
    main()
    