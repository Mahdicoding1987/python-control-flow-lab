def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

#exercise1

vowel = ("a", "e", "i", "o", "u")

letter = ("c")

def check_letter():

    if letter in vowel:
        print(letter, "is a vowel")
    else:
        print(letter, "is not a vowel")

check_letter()

#exercise2

age = 12

def check_voting_eligibility():

    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote.")

check_voting_eligibility()

#exercise3

dog_age = 3

def calculate_dog_years():

    if dog_age <= 2:
        dog_years = dog_age * 10
        print("The dog's age in human years is:", dog_years)
    else:
        dog_years = 20 + (dog_age - 2) * 7
        print("The dog's age in human years is:", dog_years)

calculate_dog_years()

#exercise4

cold = True
rainy = True

def weather_advice():

    if cold and rainy:
            print("Wear a waterproof coat.")
    elif cold and not rainy:
            print("Wear a warm coat.")
    elif not cold and rainy:
            print("Carry an umbrella.")
    else:
            print("Wear light clothing.")

weather_advice()

#exercise5

month = "Oct"
day = 12

def determine_season():

    if month in ["Dec", "Jan", "Feb", "Mar"]:
        if month == "Dec" and day < 21:
            season = "Fall"
            print("The season is", season)
        elif month == "Mar" and day > 19:
            season = "Spring"
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