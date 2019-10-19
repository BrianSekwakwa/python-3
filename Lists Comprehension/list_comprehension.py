# // LIST COMPREHENSIONS

# nums = [1,2,3,4,5,6,7]

# new_nums = [num * 10 for num in nums]

# print(new_nums)

# names = ["brian","steve","allen","josh"]

# capitalized_names = [name.capitalize() for name in names]

# print(capitalized_names)

# / Lists Comprehension with Conditional Logic

# numbers = [1,2,3,4,5,6]

# evens = [num for num in numbers if num % 2 == 0]

# odds = [num for num in numbers if num % 2 != 0]

# print(evens,odds) 

# / Nested Lists, basically lists within lists

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for item in nested_list:
  for num in item:
    print(f"{num} comes from this list: {item}")