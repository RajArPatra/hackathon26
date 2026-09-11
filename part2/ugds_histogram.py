"""
ugds_histogram.py
Authors: <your name(s) here>
Created: 2026-09-11
Model 3, Question 20: plot a histogram of the UGDS column
("Enrollment of undergraduate certificate / degree-seeking students")
from the College Scorecard data (scorecard.csv). UGDS is column KE,
which is index 290 in each row. NULL values are skipped.
"""

# a) two import statements
import csv
import matplotlib.pyplot as plt

# b) three statements that prepare the csv file for reading
infile = open("scorecard.csv")
data = csv.reader(infile)
names = next(data)  # skip/store the header row of column names

# c) + d) read the whole UGDS column into a list, converting to int,
#          leaving out the "NULL" values
ugds = []
MISSING = {"NULL", "NA", ""}   # markers used for missing data in the file
for row in data:
    value = row[290]           # the UGDS cell for this school
    if value not in MISSING:   # skip missing values
        ugds.append(int(float(value)))  # csv values are strings

infile.close()

# e) the last two lines that plot and show the histogram
plt.hist(ugds, 50)
plt.show()
