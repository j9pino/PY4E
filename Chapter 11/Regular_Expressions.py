# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
    # Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
    # Actual data: http://py4e-data.dr-chuck.net/regex_sum_1658577.txt (There are 70 values and the sum ends with 689)
# The basic outline of this problem is to read the file, look for integers using the re.findall().
# Look for a regular expression of '[0-9]+' and then convert the extracted strings to integers and sum up the integers.

# import regex library and open assignment file
import re
hand = open('actual_sum.txt')

# create an empty list to collect any numbers in the text
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    # print(stuff) to view extracted numbers
    # convert numeric strings into integers and add to list; sum up list of values
    for value in stuff:
        num = int(value)
        numlist.append(num)
print('Total:', sum(numlist))

