# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:54:43 2022

@author: 2163010
"""
#helloo world
print("Hello World!")

#this prgrm add two numbers
num1=1.5
num2=2.4
#Add 2 no's
sum=num1+num2
#display the sum
print("the sum of {0} and{1} is {2}".format(num1,num2,sum))



#square root of a number
num=int(input("enter a number:"))
sqrt=num**0.5
print("square root is:",sqrt)

import math
number=int(input("enter a number:"))
sqrt=math.sqrt(number)
print("square root:",sqrt)

#Calculate Area Of Triangle
a=5
b=6
c=7
#calculate the semiperimeter
s=(a+b+c)

area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of the triangle is %0.2f'%area)

#Quadratic equation aX2+bX+c=0

import math
a=1
b=5
c=6
#calculate the dicriment
d=(b**2)-(4*a*c)
#finding 2 sol's
sol1=(-b-math.sqrt(d))/(2*a)
sol2=(-b+math.sqrt(d))/(2*a)
print("The Solution are {0} and{1}".format(sol1,sol2))

#swapping of 2 no's
x=5
y=10
temp=x
x=y
y=temp
print("the value of x after swapping:{}".format(x))
print("the value of y after swapping:{}".format(y))

#Random numbers
import random
print(random.randint(1,8))

# Python program to convert kilometer to miles
 
# take input from user
kilometers = float(input("Enter value in kilometers: "))
 
# calculate miles
meter = kilometers * 1000.0


# Python program to convert kilometer to miles
 
# take input from user
kilometers = float(input("Enter value in kilometers: "))
 
# calculate miles
meter = kilometers * 1000.0
 
print('%0.2f kilometers is equal to %0.2f meters' %(kilometers,meter))

#Celsius to Fahrenheit
celsius=float(input("enter  temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print('%.2f celsius is:%0.2f fahrenheit'%(celsius,fahrenheit))

#print output without new line
print('gayathri')
print('welcome to cognizant!')
#new line
print()
#print both stmts in a single line
print('Gayathri',end="")
print('welcome to cognizant!')






