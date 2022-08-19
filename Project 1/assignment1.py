# Name: Matthew Armstrong
# OSU Email: armstrm2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: # 1
# Due Date: April 18th
# Description: Python Fundamental Review Assignments

import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """TODO:
    returns a Python tuple with two values, the min & max of the input array"""

    # initialize and set the min/max values
    arr_min = arr.get(0)
    arr_max = arr.get(0)

    # iterate the array
    for idx in range(arr.length()):
        # check for the min value
        if arr.get(idx) < arr_min:
            arr_min = arr.get(idx)
        # check for the max value
        if arr.get(idx) > arr_max:
            arr_max = arr.get(idx)
    return arr_min, arr_max

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """TODO:
    Returns new StaticArray object within content of original array."""
    length = arr.length()
    new_arr = StaticArray(length)  # create a StaticArray
    for idx in range(length):
        # determine if the number is divisible by 3
        if arr[idx] % 3 == 0 and arr[idx] % 5 != 0:
            new_arr.set(idx, "fizz")
        # determine if the number is divisible by 5
        elif arr[idx] % 5 == 0 and arr[idx] % 3 != 0:
            new_arr.set(idx, "buzz")
        # determine if the number is both a multiple of 3 and a multiple of 5
        elif arr[idx] % 3 == 0 and arr[idx] % 5 == 0:
            new_arr.set(idx, "fizzbuzz")
        # the element in the new array will have the same value as in the original array.
        else:
            new_arr.set(idx, arr.get(idx))
    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """TODO: function that receives a StaticArray,
    and reverses the order of the elements in the array."""
    len = arr.length()
    for idx in range(len // 2):
        temp = arr.get(idx)
        # swapping values
        arr.set(idx, arr.get(len - idx - 1))
        arr.set(len - idx - 1, temp)
    pass

# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """TODO:
    Returns a new StaticArray, where all of the elements are from the original array,
    but their position has shifted right or left steps number of times."""

    length = arr.length()
    new_arr = StaticArray(length)  # create a new StaticArray
    steps %= length  # calculation

    for idx in range(length):
        new_arr.set(idx, arr.get(idx))
    # rotating right
    if steps > 0:
        for idx in range(length):
            new_arr.set((idx + steps) % length, arr.get(idx))
    # rotating left
    elif steps < 0:
        for idx in range(arr.length()):
            new_arr.set((idx + steps) % length, arr.get(idx))
    return new_arr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """TODO:
    Returns a StaticArray that contains all the consecutive integers
    between start and end (inclusive)."""
    length = abs(end-start) + 1
    new_arr = StaticArray(length)  # create a new StaticArray
    # ascending array
    if start <= end:
        for idx in range(length):
            new_arr.set(idx, start + idx)  # increment
    # descending array
    if start > end:
        for idx in range(length):
            new_arr.set(idx, start - idx)
    return new_arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """TODO:
    Returns an integer that describes whether the array is sorted.
    The method must return: 1 if ascending, -1 if descending, 0 otherwise"""
    ascending = 0
    descending = 0
    length = arr.length()

    if length == 1:
        return 1

    for idx in range(0, length - 1):
        if arr.get(idx) < arr.get(idx + 1):
            ascending += 1
        elif arr.get(idx) > arr.get(idx + 1):
            descending += 1

    # return 1 if the array is sorted in strictly ascending order.
    if ascending == (length - 1):
        return 1
    # return -1 if the list is sorted in strictly descending order.
    elif descending == (length - 1):
        return -1
    # return 0 otherwise.
    else:
        return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------


def find_mode(arr: StaticArray) -> tuple:
    """TODO:
    Receives a StaticArray, that is sorted in order,
    either non-descending or non-ascending."""
    length = arr.length()

    most_occurred = arr.get(0)
    count = 1

    mode = most_occurred
    frequency = 1

    for idx in range(1, length):
        if arr.get(idx) == most_occurred:
            count += 1
        else:
            if count > frequency:
                mode = most_occurred
                frequency = count
            most_occurred = arr.get(idx)
            count = 1
    if count > frequency:
        mode = most_occurred
        frequency = count
    return mode, frequency

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """TODO: remove duplicates function"""
    count = 0  # create counters
    length = arr.length()

    for idx in range(1, length):
        if arr.get(idx) == arr.get(idx-1):
            count += 1
    # create a new StaticArray
    new_arr = StaticArray(length - count)
    new_arr[0] = arr[0]

    new_count = 1
    # populate new_array and check duplicate
    for val in range(1, length):
        # increment the index
        if arr.get(val) != arr.get(val-1):
            new_arr.set(new_count, arr[val])
            new_count += 1
    return new_arr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO:
    Returns a new StaticArray with the same content sorted
    in non-ascending order, using the count sort algorithm.
    The original array must not be modified.
    O(n+k) time complexity.
    """
    # initialize the min/max values in the array
    min_value = min_max(arr)[0]
    max_value = min_max(arr)[1]
    # create a new output array
    length = arr.length()
    output_arr = StaticArray(arr.length())
    # create a count array
    count_range = max_value - min_value + 1
    count_arr = StaticArray(count_range)
    # set to 0, generate a count
    for idx in range(0, count_range):
        count_arr.set(idx, 0)
    # start counting
    for idx in range(0, length):
        count_arr[count_range - (arr[idx] - min_value) - 1] += 1
    # change count_arr position
    for idx in range(1, count_range):
        count_arr[idx] += count_arr[idx - 1]
    # print array
    for idx in range(length):
        output_arr[count_arr[count_range - (arr[idx] - min_value) - 1] - 1] = arr[idx]
        count_arr[count_range - (arr[idx] - min_value) - 1] -= 1
    return output_arr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO:
    Returns a new StaticArray with squares of the values from the original array,
    sorted in non-descending order.
    The original array should not be modified."""
    # create & initialize a new array
    length = arr.length()
    new_arr = StaticArray(length)
    # initialize and keep track of count values
    count = length - 1
    left = 0
    right = length - 1

    for idx in range(0, length):
        if abs(arr[left]) >= abs(arr[right]):
            new_arr[count] = arr[left] ** 2
            left += 1
        else:
            new_arr[count] = arr[right] ** 2
            right -= 1
        count -= 1

    return new_arr

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]}, Max: {result[1]}")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        print(f"Min: {result[0]: 3}, Max: {result[1]}")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        mode, frequency = find_mode(arr)
        print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
