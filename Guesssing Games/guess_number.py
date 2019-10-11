from random import randint

is_playing = True
randNumber = randint(1, 10)

while is_playing:
    print("Guess the number between 1 to 10")
    answer = int(input())

    if answer == randNumber:
        print("Correct! you got it right")
        play_again = input("Do you want to play again (y/n): ")
        if play_again == "y":
            randNumber = randint(1, 10)
        else:
            print("Thanks for playing. Bye!")
            is_playing = False
    elif answer < randNumber:
        print("Your answer is too low")
    elif answer > randNumber:
        print("Your answer is too high")
