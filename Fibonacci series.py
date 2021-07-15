# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def Fibonacci(Number):
    if(Number<0):
        print("enter whole number")

    elif(Number == 0):
        return 0
    elif(Number == 1):
        return 1
    else:
        return (Fibonacci(Number - 2) + Fibonacci(Number - 1))

n = int(input("Enter the value of 'n': "))
print("Fibonacci Series:")
for n in range(0, n):
  print(Fibonacci(n))
        
