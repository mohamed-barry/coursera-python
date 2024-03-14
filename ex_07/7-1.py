# Write a program that prompts for a file name,
# then opens that file and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
new_words = ""


for word in inp:
    new_words += word.upper()
    new_words.rstrip()
print(new_words)
