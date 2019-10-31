# // MAP

# A standard function that accept two arguments
# The arguments have to be a function and an "iterable"
# Iterable - something that can be looped over

# Example 
nums = [1,2,3,4]

doubles = list(map(lambda x: x*2, nums))

print(doubles)
