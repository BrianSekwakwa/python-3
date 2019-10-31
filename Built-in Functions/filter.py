# // FILTER

# There is a lambda fir each value in the iterable
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda

# Example

nums = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x % 2 == 0, nums))

print(even) 