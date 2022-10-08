# Write code using find() and string slicing (see section 6.10) to extract the number from the variable "text". 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
num = text[pos+1:]
fnum = float(num)
print(fnum)