#QUESTION : 1
'''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are'''

print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are'''")

#QUESTION:2
#Print the python version
import platform
print(platform.python_version())

#QUESTION:3
#Show curent date and time
import datetime
print(datetime.datetime.now())

#QUESTION:4
#Calculate the area of Circle
import math
radius=int(input("Enter the radius of Circle = "))

area=(math.pi*radius*radius)
print("The area of circle is: ",area)


#QUESTION :5
#First name and Last Name
fname=str(input("Enter First Name: "))
lname=str(input("Enter Last Name: "))
print(lname+" "+fname)

#QUESTION:6
#Addition
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=a+b
print("The Addition of two numbers is: ",c)
