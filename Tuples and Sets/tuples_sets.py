# // TUPLES
# - An ordered collection or grouping of items
# - It cannot be mutated, meaning it cannot be changed
# - A way to store data that will not be changed

# Example

# numbers = (1, 2, 3, 4)

# print(numbers)

# Example
# - Using tuples as keys in a dcitionary

# age_range = {
#     (0, 12): "children",
#     (13, 21): "teenagers",
#     (22, 35): "young adults",
#     (35, 50): "middle aged adults",
#     (50, 100): "senior citizen"
# }

# print(age_range.keys())

# / Methods for Tuples

# numbers = (1, 2, 3, 4)

# for num in numbers:
#   print(num)

# numbers = (1, 2, 2, 2, 2, 2, 2, 3, 4)

# / Count - tells us how many items are in a tuple

# print(numbers.count(5))

# / index - returns the index in which the value is found in the tuple

# index = numbers.index(2)

# print(index)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# // SETS
# - a collection of data that is unique and doesnt have any duplicate values
# - Elements in sets are not ordered
# - You cannot access items in a set by index

# Example 

# number_set = {1,2,3,4,5,6,7,7,7,7}

# for num in number_set:
#   print(num)

# / Methods for sets

# number_set = {1,2,3,4,5,6,7,7,7,7}

# / add - adds an element to a set. if the element is already in the set, the set doesn't change.

# number_set.add(11)
# number_set.add(7)
# print(number_set)

# / remove - removes a value from the set - returns a keyError if the value is not found

# number_set.remove(7)
# print(number_set)

# / discard - removes a value from the set but doesn't throw an error

# number_set.discard(10)
# print(number_set)

# / copy - creates a copy of the set but they are not stored at the place in memory

# new_set = number_set.copy()
# print(new_set == number_set)

# / clear - removes all the contents if the set

# number_set.clear()
# print(number_set)

# / Set Math

# first_class = {
#   "brian",
#   "karen",
#   "steve",
#   "bob",
#   "frank",
#   "luffy",
#   "robin"
# }

# second_class = {
#   "nami",
#   "usopp",
#   "chopper",
#   "robin",
#   "sanji",
#   "zoro",
#   "frank"  
# }

# - Set Union - Generates a set with all unique items
# set_union = first_class | second_class

# - Set Intersection - Generates a set with common items in both sets
# set_union = first_class & second_class

# print(set_union)

# / SET COMPREHENSION

# number_set = {1,2,3,4,5,6,7,7,7,7}

# new_set = {x ** 2 for x in number_set}

# print(number_set)
# print(new_set)
