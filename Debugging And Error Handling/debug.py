# // Common Python Errors

# SyntaxError - wrong syntax python cannot understand
# NameError - When a variable is not defined
# TypeError - Operation applied to the wrong type
# IndexError - When you try to access an item in list with the wrong index
# ValueError - Built-in function that receives the right type of argument but an inappropriate value
# KeyError - When a dictionary does not have a specific key
# AttributeError - Occurs when a variable does not have an attribute

# // Raising Your Own Error

# Using the keyword "raise" to cause an error 

# Example 

# raise NameError("name is not defined")

# // Handling Errors 

# try:
#   name
# except NameError:
#   print("Big Problem")

# try:
#   runs this portion of code first and checks to see if there is an error somewhere
# except:
#   if there is an error it will be ran here
# else:
#   runs if the except code block doesn't run
# finally:
#   runs no matter what

# // Debugging With PDB

from pdb import set_trace

first = "first"
second = "second"
set_trace()
result = first + second
third = "third"
result += third
print(result)

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)