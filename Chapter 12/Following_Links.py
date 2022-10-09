# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below. 
# Extract the href= vaues from the anchor tags, and scan for a tag that is in a particular position relative to the first name in the list.
# Follow that link and repeat the process a number of times and report the last name you find.
# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
    # Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
    # Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
    # Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Jaye.html
    # Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
    # Hint: The first character of the name of the last page that you will load is: B

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Request position and count input
position = int(input('Enter position: '))-1 
count = int(input('Enter count: '))
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Jaye.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Create a list of tags and print according to position and count input
sequence = []
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)

# Print answer
print(sequence[-1])

