# // MODULES

# Keeps python files small
# Reuse code across multiple files by importing
# A module is just a python file that can be used in other python files

# import file1
# import file2 

# print(file1.greeting())
# print(file2.fav_color())

# // The mysterious __name__ variable

# Every python file has a __name__ variable
# If the file is the main file being run its value is __main__
# Otherwise, its value is the file name

# import file1

# def say_hello():
#   print(f"Hello, my __name__ is {__name__}")

# print(file1.greeting())
# say_hello()