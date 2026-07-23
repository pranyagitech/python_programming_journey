a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("It is an Equilateral Triangle!")
    
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle!")
    
    else:
        print("It is a Scalene Triangle!")

else:
    print("!!!Invalid Triangle!!!")
