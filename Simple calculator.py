#calculator

a= int(input("Enter 1st number"))
b= int(input("Enter 2nd number"))

o= input("Choose opreator")

if o == "+":
    c= a+b
    print(int(c))

elif o == "-":
    c= a-b
    print(int(c))

elif o == "*":
    c= a*b
    print(int(c))

elif o == "/":
    c= a/b
    print(int(c))

else:
    print("Wrong choice")