import os

"""
PROBLEM 1

You are provided with a dataset. Your challenge consists of the following two parts

--- Part One ---
Find the two entries that sum to 2020 and then multiply those two numbers together.
For example, suppose your dataset contained the following:

1721  
979  
366  
299  
675  
1456

In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
Of course, your actual dataset is much larger.
Find the two entries that sum to 2020; what do you get if you multiply them together?

"""


def find_two_numbers_product(numbers, target):
    """
    Find two numbers in a list that add up to a target value.
    :param numbers: list of integers
    :param target: integer
    :return: list of product of two numbers

    It is not specified in the question if the pair is unique or not
    so I'm building the solution to return product of all the pairs that add up to the target value.

    In case these is a unique solution, then the list will have only one element
    In case there are duplicates in the list, then the same pair can appear multiple times also

    """
    pairs = []
    seen = set()
    products = []

    # add condition for empty list
    if len(numbers) < 2:
        return products, pairs

    for num in numbers:
        diff = target - num

        if diff in seen:
            pairs.append((num, diff))
            products.append(num * diff)
        else:
            seen.add(num)

    return products, pairs


"""
PROBLEM 2

--- Part Two ---
Find three numbers in your dataset that meet the same criteria.
Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
Multiplying them together produces the answer, 241861950.
In your dataset, what is the product of the three entries that sum to 2020?

"""


def find_three_numbers_product(numbers, target):
    """
    Find three numbers in a list that add up to a target value.
    :param numbers: list of integers
    :param target: integer
    :return: list of product of three numbers

    It is not specified in the question if the triplet is unique or not
    so I'm building the solution to return product of all the triplets that add up to the target value.

    In case these is a unique solution, then the list will have only one element
    In case there are duplicates in the list, then the same triplet can appear multiple times also

    """
    triplets = []
    triplet_products = []

    # add condition for empty list
    n = len(numbers)
    if n < 3:
        return triplet_products, triplets

    for i, num in enumerate(numbers):
        if i > n - 3:
            continue

        diff = target - num
        _, pairs = find_two_numbers_product(numbers[i + 1 :], diff)

        for pair in pairs:
            triplets.append((num, pair[0], pair[1]))
            triplet_products.append(num * pair[0] * pair[1])

    return triplet_products, triplets


if __name__ == "__main__":

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(ROOT_DIR, "data", "input")
    FILE_PATH = os.path.join(DATA_PATH, "input_numbers.txt")
    print(FILE_PATH)

    TARGET = 2020

    # Read the file
    with open(FILE_PATH, "r") as file:
        data = file.read()
        numbers = data.split("\n")

    # Convert the numbers to integers
    numbers = [int(number) for number in numbers]

    pair_product, pairs = find_two_numbers_product(numbers, TARGET)
    print(pair_product, pairs)

    triplet_product, triplets = find_three_numbers_product(numbers, TARGET)
    print(pair_product, triplets)
