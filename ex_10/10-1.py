# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith("From"):
        continue
    words = line.split()
    if not len(words) > 5:
        continue
    time = words[5]
    hr = time[:2]
    counts[hr] = counts.get(hr, 0) + 1


for k, v in sorted(counts.items()):
    print(k,v)


