import random

num = random.randint(0,10)
# print("The num is: ", num)

age = int(input("Please enter your guess number, the number is in 0 ~ 10: "))

count = 1

while count <3:
    if age == num:
        print("You're lucky, it's correct!")
        break
    count += 1
    age = int(input("You guess error, please enter your guess number again: "))

while count == 3:
    is_want = input("Do you want to continue, yes or no: ")
    if is_want == "Y" or is_want == "y":
        count = 0
        while count < 3:
            if age == num:
                print("You're lucky, it's correct!")
                break
            count += 1
            age = int(input("You guess error, please enter your guess number again: "))
    elif is_want == "N" or is_want == "n":
        exit()
