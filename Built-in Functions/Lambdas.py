# Lambdas are nameless functions that can be passed in to other functions
# It only takes up one line 

# Example

def greet():
  """A function that greets the user"""
  print("Hello world, normal")

greeting = lambda : print("Hello World, lambda")

print(greeting)