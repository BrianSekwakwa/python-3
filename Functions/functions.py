# // FUNCTIONS
# - A process for excuting a task
# - It can accept input and return output
# - Useful for executing similar procedures over and over again
# - Helps us stay DRY (Dont Repeat Yourself)
# - Prevents code duplication
# - Abstracts away code for common methods used all the time

# Example

# def say_hi():
#   print("Hi!")

# say_hi()
# say_hi()
# say_hi()
# say_hi()


# / Returning values from functions
# - The return keyword exists the function
# - Outputs whatever value you put after the return keyword
# - Pops the function off of the call stack

# def squared_number(number):
#     results = number ** 2
#     return results


# addition = 10 + squared_number(5)
# print(addition)

# from random import randint

# results = randint(0, 1)

# def coin_flip(random):
#     if random == 0:
#       print("Heads...")
#     else:
#       print("Tails...")

# coin_flip(results)

# / Keyword Arguments

# def full_name(first="Brian", last="Sekwakwa"):
#   message = f"Your name is {first} {last}"
#   return message

# print(full_name(last="Dumbledore", first="albert"))

# / Scope - The accessibility of variables

# name = "Steve"
  
# def greet():
#     global name
#     name += " Balmer"
#     print(f"Hey {name}, How are you doing?")

# greet()

# / Documenting Functions

# def say_hello():
#   """A simple documentation for a function"""
#   return "Hello!"


# print(say_hello.__doc__)

# / *args (star arguments)

# A special operator we can pass to functions
# Gathers remaining arguments as a tuple

# Example 

# def sum_all_nums(*args):
#   summed = 0
#   for num in args:
#     summed += num

#   return summed

# print(sum_all_nums(1,2,3,4,5,6))

# / **kwargs

# A special operator we can pass to functions
# Gathers remaining keyword arguments as a dictionary


# Example

# def fav_color(**kwargs):
#   name = kwargs["name"]
#   age = kwargs["age"]
#   color = kwargs["fav_color"]
#   message = f"The name of the user is {name}, the user is {age} years old and favorite color is {color}"

#   print(message)

# fav_color(name="brian",age=25,fav_color="blue")

# / Ordering Parameters

# 1. parameters
# 2. *args
# 3. defaults parameters
# 4. **kwargs

# / Tuple Unpacking

# def sum_all_values(*args):
#   total = 0
#   print(args)
#   for num in args:
#     total += num
#   print(total)

# nums = [1,2,3,4,5,6]

# print(*nums)
# sum_all_values(*nums)

# / Dictionary Unpacking

# def names(first,second):
#   message = f"Hey there {first} and {second} how are you doing today"
#   print(message)

# user_names = {
#   "first": "colt",
#   "second": "Rusty"
# }

# names(**user_names)