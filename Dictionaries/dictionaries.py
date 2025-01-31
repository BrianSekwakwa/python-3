# // DICTIONARIES

# / they are data structures that consists of key value pairs
# / Keys to describe our data and values to represent the data

# / Example

# instructor = {
#   "name": "colt",
#   "owns_dog": True,
#   "num_courses": 4,
#   "favorite_language": "python",
#   "is_halarious": False,
#   44: "my favorite number!"
# }

# print("name" in instructor)

# / Using the dict() method to create a dictionary

# person = dict(name="brian", age=25, is_male=True)
# print(person)

# / Iterating Dictionaries

# instructor = {
#   "name": "colt",
#   "owns_dog": True,
#   "num_courses": 4,
#   "favorite_language": "python",
#   "is_halarious": False,
#   44: "my favorite number!"
# }

# for value in instructor.values():
#   print(value)

# for key in instructor.keys():
#   print(key)

# print("Instructor Details: \n")
# for key,value in instructor.items():
#   print(f"{key}: {value}")

# // DICTIONARY METHODS

instructor = {
  "name": "colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "python",
  "is_halarious": False,
  44: "my favorite number!"
}

# / Clear - clears all the keys and values in the dictionary

# print(instructor)
# instructor.clear()
# print(instructor)

# / Copy - makes a copy of a dictionary

# copy = instructor.copy()

# print (copy is instructor) # False, do not exist at the same place in memory

# / fromkeys() - makes a dictionary from given keys, used to generate default dictionaries

# user = ["name", "age", "is_male", "phone_number"]

# new_user = {}.fromkeys(user, "unkwown")

# print(new_user)

# / get() - retrieves a key in an object and return None instead of a KeyError if the key does not exist

# print(instructor.get("crime"))

# / Pop - takes a key as an argument and removes the key-value pair from the dictionary

# print(instructor)
# print()
# instructor.pop("name")
# print(instructor)

# / Popitem - removes a random key in the dictionary

# print(instructor)
# print()
# instructor.popitem()
# print(instructor)

# / update - updates the keys and values in a dictionary with another set of key value pairs

# more_info = {
#   "last_name": "steele",
#   "age": 35,
#   "is_american": False
# }

# instructor.update(more_info)
# print(instructor)

# // DICTIONARY COMPREHENSION

# { __ : __ for __ in ___ }

# Example


# numbers = {
#   "first": 1,
#   "second": 2,
#   "third": 3
# }

# squared_numbers = {keys + "_number" for keys in numbers.keys()}

# print(squared_numbers)