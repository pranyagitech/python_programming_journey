angle = int(input("Enter the angle in degrees: "))

if angle < 90:
    print("It is an Acute Angle!")

elif angle == 90:
    print("It is a Right Angle!")

elif angle < 180:
    print("It is an Obtuse Angle!")

elif angle == 180:
    print("It is a Straight Angle!")

else:
    print("!!!Invalid Angle!!!")
