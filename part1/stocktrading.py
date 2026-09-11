"""
stocktrading.py
Authors: Raj Aaryaman Patra
Created: 2026-09-11
maxProfit(prices) returns the maximum profit from buying on one day and
selling on a LATER day. Returns 0 if no profit is possible. Includes a
small test suite (black-box and clear-box cases).
"""


def maxProfit(prices):
    """Return the best profit from a single buy-then-later-sell."""
    if not prices:              # no data -> no profit
        return 0
    min_price = prices[0]       # lowest price seen so far (a buy day)
    best = 0                    # best profit found so far
    for price in prices[1:]:    # each later day is a candidate sell day
        best = max(best, price - min_price)
        min_price = min(min_price, price)
    return best


def test_maxProfit():
    """Tests covering different scenarios (black-box + clear-box)."""
    # Black-box: assignment example.
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    # Black-box: strictly decreasing -> no profit.
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    # Clear-box: empty list edge case.
    assert maxProfit([]) == 0
    # Clear-box: single element (can't sell after buying).
    assert maxProfit([5]) == 0
    # Black-box: lowest price is last, so no valid later sell -> 0.
    assert maxProfit([5, 4, 3, 2, 1]) == 0
    # Clear-box: best buy is the global minimum in the middle.
    assert maxProfit([3, 8, 1, 9]) == 8
    print("All maxProfit tests passed.")


def main():
    test_maxProfit()


if __name__ == "__main__":
    main()
