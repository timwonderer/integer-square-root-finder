"""
Integer Square Root Finder

This program estimates the integer square root of a given number using:
- Ending digit elimination (numbers ending in 2, 3, 7, 8 cannot be perfect squares).
- Digit-based range estimation to reduce the search space.
- Binary search to narrow the interval for potential square roots.
- Linear search to finalize the result.

It supports both positive and negative inputs (reporting imaginary roots for negatives).
"""

import sys
import time

def endingTest(num):
    """
    Checks whether the last digit of num makes an integer square root impossible.

    Args:
        num (int): non‑negative integer to test.

    Returns:
        bool: False if last digit is in ("2", "3", "7", "8")—no square ends with those;
              True otherwise (further testing needed).
    """
    print("Now checking the input for ending that won't have integer roots\n")
    if str(num)[-1] in ("2", "3", "7", "8"):
        print(f"This number ends in {str(num)[-1]}. No known number when squared will result in that number.\n")
        print("No integer root found\n")
        return False
    return True

def binarySearch(num):
    """
    Narrows down the possible range [low, high] for the integer root based on the digit count of num.

    Args:
        num (int): non‑negative integer to search.

    Returns:
        list: [flag, low, high], where
            - flag False: exact root found during narrowing (low == high)
            - flag True: need final scan between low and high
    """
    print("Now checking for the range where integer root could be found\n")
    count = len(str(num))
    if count % 2 != 0:
        ceiling = 10 ** ((count // 2) + 1)
        floor = 10 ** (count // 2)
    else:
        ceiling = 10 ** (count // 2)
        floor = 10 ** ((count // 2) - 1)

    high, low = ceiling, floor
    print(f"Beginning range is between {low} and {high}\n")

    while high - low > 10:
        mid = (low + high) // 2
        if mid ** 2 == num:
            return [False, mid, mid]
        elif mid ** 2 > num:
            high = mid
        else:
            low = mid

    return [True, low, high]

def squareTest(num, low, high):
    """
    Linearly checks each integer from low to high (inclusive) to find an exact square root.

    Args:
        num (int): non‑negative integer whose root we seek.
        low (int): lower bound of search (inclusive).
        high (int): upper bound of search (inclusive).

    Returns:
        int or None: The integer root if found; otherwise None.
    """
    print(f"Begin squaring every number from {low} to {high}\n")
    for i in range(low, high + 1):
        square = i ** 2
        if square == num:
            return i
        elif square > num:
            print("No integer root found\n")
            return None
    return None

def display_root(original, root):
    """
    Handles output formatting for the root.

    Args:
        original (int): The original input number.
        root (int or None): The integer root found.
    """
    if root is None:
        return
    result = f"{root}i" if original < 0 else str(root)
    print(f"The square root of {original} is {result}\n")

def findIntegerRoot(original):
    """
    Coordinates the integer-root search: handles trivial cases, applies endingTest,
    chooses between direct scan or binary+scan, and prints the result.

    Args:
        original (int): the input integer (may be negative).
    """
    print(f"Searching for integer root of {original}\n")
    if original in (0, 1, -1):
        display_root(original, abs(original))
        return

    testVal = abs(original)
    if not endingTest(testVal):
        return

    if testVal <= 1000000:
        root = squareTest(testVal, 1, (testVal // 2) + 1)
    else:
        proceed = binarySearch(testVal)
        if not proceed[0]:
            display_root(original, proceed[1])
            return
        root = squareTest(testVal, proceed[1], proceed[2])

    display_root(original, root)

def userInput():
    """
    Prompts the user to enter an integer and validates the input.

    Returns:
        tuple: (userNumber, repeat_flag)
            - userNumber (int or None): parsed integer or None if invalid
            - repeat_flag (bool): True if input was invalid (retry), False otherwise
    """
    try:
        userNumber = int(input("Enter an integer to find its integer root: "))
    except ValueError:
        print("That is an invalid entry. Try again.\n")
        return None, True
    else:
        print("-----------------------------")
        return userNumber, False

def main():
    """
    Main loop: keeps prompting until valid input,
    measures the time to find the integer root,
    and reports elapsed time.
    """
    repeat = True
    while repeat:
        testVal, repeat = userInput()

    start_time = time.perf_counter()
    findIntegerRoot(testVal)
    end_time = time.perf_counter()

    print("-----------------------------")
    print("End of integer root search.\n")
    print(f"Time used: {end_time - start_time:.9f} seconds")

if __name__ == "__main__":
    main()
