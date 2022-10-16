# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
    # Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    # Actual data: http://py4e-data.dr-chuck.net/comments_1658582.json (Sum ends with 32)

import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
print('Retrieving: ', address)
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved: ', len(data), 'characters')

total = 0

info = json.loads(data)
number = info['comments']
for item in number:
    number = item['count']
    total = total + int(number)

print ('Count: ', number)
print ('Sum: ', total)