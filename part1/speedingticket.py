"""
speedingticket.py
Authors: Raj Aaryaman Patra
Created: 2026-09-11
Given a speed limit and a driving speed (mph), print the traffic ticket amount.

Ticket rules:
  - 10 mph or more UNDER the limit .......... $50
  - 6 - 20 mph OVER the limit ............... $75
  - 21 - 40 mph OVER the limit .............. $150
  - more than 40 mph OVER the limit ......... $300
  - otherwise (5 under .. 5 over) ........... $0  (no ticket)
"""


def ticket_amount(limit, speed):
    """Return the ticket amount (int) for a given speed limit and speed."""
    over = speed - limit  # positive => over the limit, negative => under
    if over <= -10:          # 10 mph under or slower
        return 50
    elif 6 <= over <= 20:    # 6-20 over
        return 75
    elif 21 <= over <= 40:   # 21-40 over
        return 150
    elif over > 40:          # faster than 40 over
        return 300
    else:                    # from 9 under up to 5 over -> no ticket
        return 0


def main():
    # No prompt text, per the assignment note.
    limit = int(input())
    speed = int(input())
    print(ticket_amount(limit, speed))


if __name__ == "__main__":
    main()
