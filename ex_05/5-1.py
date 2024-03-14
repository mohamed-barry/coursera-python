total = 0.0
count = 0

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Input")
    total = total + fval
    count = count + 1

print(total, count, total / count)
