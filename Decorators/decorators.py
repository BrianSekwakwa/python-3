# // DECORATORS

# Decorators are functions
# Decorators wrap other functions and enhance their behavior
# Decorators are examples of higher order functions
# Decorators have their own syntax, using "@" (syntactic sugar)

def be_polite(fn):
  def wrapper():
    print("What a pleasure to meet you!")
    fn()
    print("Have a great day!")
  return wrapper

@be_polite
def greet():
  print("Hi my name is Brian")


print(greet())