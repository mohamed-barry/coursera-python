largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = int(num)
    except:
        print("Invalid Input")

    if largest is None or smallest is None:
        largest = fnum
        smallest = fnum
        print("current large", fnum)
        print("current small", fnum)
    elif fnum > largest:
        largest = fnum
        print("new large", largest)
    elif fnum < smallest:
        smallest = fnum
        print("new small", smallest)

print("Maximum is", largest)
print("Minimum is", smallest)
