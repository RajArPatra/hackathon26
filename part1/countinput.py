"""
countinput.py
Authors: Raj Aaryaman Patra
Created: 2026-09-11
countchars(st) returns the number of characters in st, excluding
spaces, periods, exclamation points, and commas. Includes a small
test suite (black-box and clear-box cases).
"""

EXCLUDED = {" ", ".", "!", ","}  # characters that must not be counted


def countchars(st):
    """Return the count of characters in st that are not space/./!/,."""
    count = 0
    for ch in st:            # walk every character in the string
        if ch not in EXCLUDED:
            count += 1
    return count


def test_countchars():
    """Tests covering different scenarios (black-box + clear-box)."""
    # Black-box: the example from the assignment.
    assert countchars("Listen, Mr. Jones, calm down.") == 21
    # Black-box: empty string edge case.
    assert countchars("") == 0
    # Clear-box: string made up ENTIRELY of excluded characters.
    assert countchars(" .!,") == 0
    # Clear-box: digits and other punctuation ARE counted.
    assert countchars("r2?") == 3
    # Black-box: no excluded characters at all -> full length.
    assert countchars("Python") == 6
    print("All countchars tests passed.")


def main():
    st = input("Enter a string: ")
    print(countchars(st))


if __name__ == "__main__":
    test_countchars()  # run tests, then the interactive program
    main()
