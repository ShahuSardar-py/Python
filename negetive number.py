#Write a Python program that prompts the user to enter a number and then checks if the number is positive, negative, or zero. If the number is positive, print "The number is positive". If the number is negative, print "The number is negative". If the number is zero, print "The number is zero

a= int(input("Enter the number"))
if a>0:
    print("The number is positive")
elif a<0:
    print("The number is negetive")
else:
    print("The number is zero")