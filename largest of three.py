a= int(input("Enter first number"))
b= int(input("Enter second number"))
c= int(input("Enter third number"))

if a>b:
    if a>c:
        print("A is largest")

if b>a:
    if b>c:
        print("B is largest")

else:
    print("C is largest")