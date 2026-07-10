p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
n = int(input("Enter time period: "))

ci = (p*(( 1 + r )**n) ) - p

print("The calculated compound interest is", ci)
