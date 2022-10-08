# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# Enter romeo.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip().split()
    for words in line:
        if words in lst: 
            continue
        else:
            lst.append(words)
lst.sort()
print(lst)