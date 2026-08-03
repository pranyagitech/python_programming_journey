temp = float(input("Enter temperature (°C): "))

if temp < 5:
    print("Cold")

elif temp < 20:
    print("Pleasant")

elif temp < 35:
    print("Warm")

else:
    print("Hot")
