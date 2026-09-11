"""
heatingcooling.py
Authors: Raj Aaryaman Patra
Created: 2026-09-11
Read a sequence of average daily temperatures and count heating days
(below 60F) and cooling days (above 80F). Input ends when the user
enters a value lower than -459 (below absolute zero in Fahrenheit).
"""


def main():
    heating = 0  # running total of heating days (temp < 60)
    cooling = 0  # running total of cooling days (temp > 80)

    while True:
        temp = int(input("Enter the average daily temperature: "))
        if temp < -459:      # sentinel: stop reading input
            break
        if temp < 60:        # cold day -> heater likely on
            heating += 1
        elif temp > 80:      # hot day -> A/C likely on
            cooling += 1
        # 60..80 inclusive counts as neither

    print("Heating days:", heating)
    print("Cooling days:", cooling)


if __name__ == "__main__":
    main()
