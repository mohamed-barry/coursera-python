hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")


try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h > 40:
    reg_pay = 40 * r
    otp = (h - 40) * (1.5 * r)
    pay = reg_pay + otp
else:
    pay = h * r
print(pay)
