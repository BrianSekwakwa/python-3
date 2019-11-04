# // What is Object Oriented Programming

# Object Oriented Programming is a method of programming that attempts to model some process or thing in the world as a "class" or "object"

# Class - a blueprint for objects

# Instance - objects that are constructed from a class blueprint that contain their class's methods and properties

# Encapsulation - The grouping of public and private attributes and methods into a programmatic class, making abstraction possible

# Abstraction - Exposing only the "relevant" data in a class interface, hiding private attributes and methods (aka the "inner workings") from users

# Example 
# - creating class and the instance of it
# class User:
#   pass

# user1 = User()

# print(user1) 

# / The __init__ method

# - This method gets executed all the time when you create a new instance of a class

# - The "self" keyword refers to the current class instance 

class User:

  @classmethod
  def say_hello(some):
    print(some)
    return "Hello I am returned"
  
  def __init__(self, first_name, last_name,age,is_male):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.is_male = is_male

  def greeting(self):
    if self.is_male:
      message = f"Good Afternoon, Mr {self.first_name} {self.last_name}"
      return message
    else:
      message = f"Good Afternoon, Mrs {self.first_name} {self.last_name}"
      return message


user1 = User("brian", "sekwakwa", 25, True)
user2 = User("lucy", "heartfelia", 16, False)
user3 = User("natsu", "dragneel", 16, True)

# print(user1.greeting())
# print(user2.greeting())
# print(user3.greeting())

print(user1.say_hello())
