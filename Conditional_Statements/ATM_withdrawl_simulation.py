balance = float(input("Enter your Bank Balance: "))

amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")
