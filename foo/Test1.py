score = float(input("Please enter your score: "))

if 90 <= score <= 100:
    print("Your score is A!")
elif 80 <= score < 90:
    print("Your score is B!")
elif 60 <= score < 80:
    print("Your score is C!")
elif 40 <= score < 60:
    print("Your score is D!")
else:
    print("Your score is E! You need to work hard!")
