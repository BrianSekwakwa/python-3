# ask for age
age = int(input("How old are you ?\n"))

# 18 - 21 wristband (cannot drink yet)
# greater than 21 legal drinking age, normal entry
# less than 18 too young to enter the club

if age >= 18 and age < 21:
    print("You are not allowed to drink and thus you will wear a wristband")
elif age >= 21:
    print("You are of legal age to drink, please enjoy yourself")
else:
    print("Sorry, you are too young for this. Go home to your mama")
