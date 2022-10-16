# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
    # Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
    # Actual data: http://py4e-data.dr-chuck.net/comments_1658581.xml (Sum ends with 42)
# You are to look through all the <comment> tags and find the <count> values sum the numbers. 
# The closest sample code that shows how to parse XML is geoxml.py. 
# But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input ('Enter url: ')
print('Retrieving: ', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved: ', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall ('comments/comment')

for item in lst:
    count = count + 1
    t = item.find ('count').text
    total = total + int(t)

print ('Count: ', count)
print ('Sum: ', total)