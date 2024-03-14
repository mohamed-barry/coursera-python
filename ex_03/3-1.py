hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

if h > 40:
    reg_pay = (40 * r)
    otp = ((h - 40) * (1.5 * r))
    pay = reg_pay + otp
else:
    pay = (h * r)
print(pay)
