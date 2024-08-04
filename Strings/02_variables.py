"""
When a programming, everything the program needs up stored in the computer's memory.
The program code it self will be stored in one area of memory, and the data it works on will be also 
stored somewhere in the memory.

"""

"""
What is a variable?

A variable is basically just a way to give a meaningful name to an area of memory, into which we
can place certain values.
"""

"""
Note:

Python variables are case sensitive, so greeting and Greeting would refer 2 different variables.
"""

greeting = "hello"

name = input("please enter your name")

"""
Python will automatically interpet the type of the variable by seeing the value we binded to it. 
"""

age = 23

print("The type of variable age is:")
print(type(age))

# we can't concatinate different types of variables in python.

print(greeting+" "+name+" is"+age+" years old")

