# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# input file and define variables
name = input('Enter file: ')
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)
counts = dict()
lst = list()

# remove whitespace and isolate email addresses
for line in handle:
    line = line.rstrip()
    if line.startswith('From '): 
        words = line.split()
        sender = words[1]
        lst.append(sender)

# count email addresses
for sender in lst:
    counts[sender] = counts.get(sender,0) + 1

# find most common email address    
bigsender = None
bigcount = None
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigsender = k
        bigcount = v
print(bigsender, bigcount)

