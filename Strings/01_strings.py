print("Today is good day")
print('How are you doing!')
print("Hello 'Dileep' how your DevOps learning is happening")
print('Hai "Ananth" my DevOps learning happening quite nicely :)')

"""
Note: In python we can use either single or dobule quotes to define a string variable.

If we start with specific type of quotes it is recommended to enclose the string value with same type of quote.


"""


# we can concatinate two strings to print a sentense.

print("Hello"+" world")


"""
we can store the strings in a variables.
"""

firstName = "Mutyala"
middleName = "Dileep"
lastName = "Raja"

print(firstName+" "+middleName+" "+lastName)

"""
Here we have used variables to store string literals and we concatinated them together to print a sentense.

"""

#=====================================================================================================================================================

"""

We can use python 'input' function to take input from the user keyboard by passing a prompt as argument and we can store the value user entered in a
variable and we can print that as shown below.

"""

greeting = "hello"
name = input("please enter your name")

print(greeting+' '+name)

"""
What we done is we called python inbuld function 'input()' which takes an string argument to provide a prompt to user to enter the value on execution of 
'input' function.

The moment user entered value for 'input' function prompt the value will be assigne to variable where the input function is assigned to.

"""

# ======================================================================================================================================================

"""
Escape character:

In python or any programming languge we can use \n to split the character sequence(string) into multiple lines.


"""

splitString = "This string has been splitted\ninto several\nlines."

print(splitString)

"""
We can use back slash to insert tab as well.

"""

tabbed = "1\t2\t3\t4\t5\t6"

print(tabbed)

"""
we can also escapte special characters using backslash.

"""

print("The pet owner said \"ussh he is sleeping\"")

# what we have did is we printed "ussh he is sleeping" in double quotes without getting error we escaped those " " inside another double quotes by using
# escape character.

"""
we can use triple quotes to escape any double quotes or single quotes python will automatically escape those quotes.

"""

print("""This is a new technology launch "Artificial Intellignce" which is going to aid human race. """)


"""
As we already know that using triple quotes we can omitt next line characters or escape characters to print multiple lines string.

"""

print("""This is a new mobile 
      which has multiple useful 
      artifical intelligence.
""")

# The same multiple line print statement can be converted into single line statement by using backslash as shown in below.

multipleLineMessage = """This is a new mobile \
which has many useful \
artifical intelligence features."""

print(multipleLineMessage)









