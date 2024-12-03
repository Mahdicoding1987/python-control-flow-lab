def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

#exercise1

# vowel = ("a", "e", "i", "o", "u")

# letter = input("Please enter a letter from the alphabet (a-z or A-Z): ").lower()

# def check_letter():

#     if letter in vowel:
#         print(letter, "is a vowel")
#     elif letter.isalpha():
#         print(letter, "is a consonant")
#     else:
#         print("Please enter a valid letter (a-z or A-Z)")

# check_letter()

#exercise2

# def check_voting_eligibility():
#     age = int(input("Please enter your age: "))

#     if age > 17:
#         print("You are eligible to vote!")
#     else:
#         print("You are not eligible to vote.")

# check_voting_eligibility()

# #exercise3

# dog_age = int(input("Please enter Dogs age: "))

# def calculate_dog_years():

#     if dog_age <= 2:
#         dog_years = dog_age * 10
#         print("The dog's age in human years is:", dog_years)
#     else:
#         dog_years = 20 + (dog_age - 2) * 7
#         print("The dog's age in human years is:", dog_years)

# calculate_dog_years()

# #exercise4

# cold = input("Its Cold?: ")
# rainy = input("Its rainy?: ")

# def weather_advice():

#     if cold and rainy:
#             print("Wear a waterproof coat.")
#     elif cold and not rainy:
#             print("Wear a warm coat.")
#     elif not cold and rainy:
#             print("Carry an umbrella.")
#     else:
#             print("Wear light clothing.")

# weather_advice()

# #exercise5

month = input("Which month is it?: ")
day = int(input("What day is it?: "))

def determine_season():

    if month in ["Dec", "Jan", "Feb", "Mar"]:
        if month == "Dec" and day < 21 or month == "Mar" and day >= 20:
            season = "Fall"
            print("The season is", season)
        else:
            season = "Winter"
            print("The season is", season)

    elif month in ["Mar", "Apr", "May", "Jun"]:
        if month == "Mar" and day >= 20 or month == "Jun" and day <= 20:
            season = "Spring"
            print("The season is", season)

    elif month in ["Jun", "Jul", "Aug", "Sep"]:
        if month == "Jun" and day >= 21 or month == "Sep" and day <= 21:
            season = "Summer"
            print("The season is", season)

    elif month in ["Sep", "Oct", "Nov", "Dec"]:
        if month == "Sep" and day >= 22 or month == "Dec" and day <= 20:
            season = "Fall"
            print("The season is", season)

    else:
        season = "Invalid month"

determine_season()