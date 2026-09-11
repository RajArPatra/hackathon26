# Part 1 - many small problems + testing  

## Guidelines

You are encouraged to work on these problems in a pair and discuss with your group. 

Each student will need to submit the files produced by their pair  (please list pair members names in the in the header docstring). You should work on one computer in the same physical location and collaborate on all problems;  splitting up work is not permitted. One person ("driver") will type the code and another ("observer") will review and evaluate it, roles should be switched every 20 minutes.

All program files should contain header docstrings with name of program author(s), creation date and brief explanation of the program,  and in-line  comments explaining what your code does.

If you can't make progress with solving a problem, please raise your hand to get help and continue working on other problems in the meantime.  

## Speeding ticket (```speedingticket.py```)
Write a program that is given two integers representing a speed limit and driving speed in miles per hour (mph) and outputs the traffic ticket amount.

Driving 10 mph *under* the speed limit (or slower) receives a  \$50 ticket. Driving 6 - 20 mph *over* the speed limit receives a \$75 ticket. Driving 21 - 40 mph *over* the speed limit receives a \$150 ticket. Driving faster than 40 mph over the speed limit receives a \$300 ticket. Otherwise, no ticket is received.

Ex: If the input is:
```
35
45
```
the output is:
```
75
```
Ex: If the input is:
```
35
26
```
the output is:
```
0
```
*Note: there are no prompts displayed by input() function.*

Thoroughly test your program. 

## Heating and cooling days (```heatingcooling.py```)

Utility company would like to have an estimate of energy requirements for a few days. If (average) temperature during a day is below 60 degrees Farenheit, that day is considered to be a heating day (people are very likely to run a heater in their houses on such day). If the temperature is above 80F, this day is considered a cooling day (people are very likely to turn on A/C on such day). Write a program that asks the user
```
Enter the average daily temperature:
```
and calculates the running totals of heating and cooling days. The program should print these two totals after all the data has been processed.
Assume that input and output types are integers. End of input is denoted by user entering a value lower than -459 (the lowest possible temperature).

Sample run:
```
Enter the average daily temperature: 33
Enter the average daily temperature: 90
Enter the average daily temperature: 98
Enter the average daily temperature: 66
Enter the average daily temperature: 22
Enter the average daily temperature: -460
Heating days: 2
Cooling days: 2
```
Thoroughly test your program. 

## Count input length without spaces, periods, exclamation points, or commas (```countinput.py```)
Write a function ```countchars(st)``` that take a string as a parameter and returns the number of characters in this string excluding spaces, periods, exclamation points, or commas.

Ex: If the arugment is:
```
Listen, Mr. Jones, calm down.
```
the return value is:
```
21
```

*Note: Account for all characters that aren't spaces, periods, exclamation points, or commas (Ex: "r", "2", "?").*

* Write a program that asks the user for input string, calls your function on that input, and displays the returned value.

* Using examples from Homework 5, add testing statements to your code. Make sure you have at least 5 tests that test different scenarios, and tests are both from black-box and clear-box categories. 



## Best time to buy and sell stock (```stocktrading.py```)

You are given a list ```prices``` where ```prices[i]``` is the price of a given stock on the ```i```th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Write a function ```maxProfit(prices)``` that calculates the maximum profit you can achieve from this transaction. If you cannot achieve any profit, the return value should be ```0```.

 

Example:
```
Argument: prices = [7,1,5,3,6,4]

Return value: 5
```
Explanation: Buy on day ```2``` (```price = 1```) and sell on day ```5``` (```price = 6```), ```profit = 6-1 = 5```.
Note that buying on day ```2``` and selling on day ```1``` is not allowed because you must buy before you sell.

Another example:

```
Argument: prices = [7,6,4,3,1]
Return value: 0
```
Explanation: In this case, no transactions are done and the max ```profit = 0```.
 
 
* Add code that tests your function. Aim for at least 5 tests that test different scenarios (both black-box and clear-box testing).  