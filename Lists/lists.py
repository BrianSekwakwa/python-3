# A collection or grouping of items
# Its better to store a single data type in a list


names = ["brian", "david", "steve", "josh", "herman"]

# THE "IN" keyword

# if "drake" in names:
#   print("the name is in the list")
# else:
#   print("the name does no exist")


# USING A FOR LOOP

# for name in names:
#     print(name)


# USING A WHILE LOOP

# index = 0

# while index < len(names):
#     name = names[index]
#     print(name)
#     index += 1

# LIST METHODS

# // How to add data to the list

# / Append adds one data at a time

# names.append("Drake")
# print(names)

# / Extend adds multiple data to a list

# names.extend(["drake", "bruce", "peter", "tony"])
# print(names)

# / Insert adds an item anyway in the lists given an index

# names.insert(0, "matuidi")
# print(names)

# // How to remove data from a list

# / Clear removes all items in the list

# print(names)
# names.clear()
# print(names)

# / Pop removes an item given a index, if no index is given it removes and returns the last item in the list

# popped_item = names.pop(0)
# print(popped_item)

# / Remove, removes an item given its value, if no item is found is throws a ValueError

# print(names)
# names.remove("brian")
# print(names)

# / Slicing, making copies of a list

new_name = names[1:5]
print(new_name)