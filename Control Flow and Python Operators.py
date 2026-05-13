# #Arithmetic operators
# # + addition, * multiplication, / division , - subtraction, // floor division, ** exponential (raise to power), % modulus
# bill = 5_000
# tax = 200
# salary = 100_000
# #addition operation
# total = bill + tax
# print(total)
#
# #subtraction operator
# difference = bill - tax
# print(difference)
#
# #multiplication operator
# multiple = bill * tax
# print(multiple)
#
# #division operator
# divide = bill / tax
# print(divide)
#
# #floor division
# floor_divide = bill // tax
# print(floor_divide)
#
# #exponetial operator (raise to power)
# expo = bill ** tax
# print(expo)
#
# #modulos operator
# mod = bill % tax
# print(mod)
# #moddulos operator will return the remaining value not divivsble by the dividing number
# fee = 5734
# mod_rem = fee % 200
# mod_div = fee / 200
# print(mod_rem)
# print(mod_div)
#
# """
# An Introduction to Modular Math
#
# When we divide two integers we will have an equation that looks like the following:
#
# A / B = Q remainder  R
#
# B  * A   ​=  Q   remainder R
#
# A divided by B equals Q  remainder R
#
# A is the dividend
# B is the divisor
# Q is the quotient
# R is the remainder
#
# Sometimes, we are only interested in what the remainder is when we divide A by B
# For these cases there is an operator called the modulo operator (abbreviated as mod) denoted by % in python programming.
#
# Using the same A, B, Q, and R as above, we would have: A % B = R
#
#
#
# We would say this as A modulo B is equal to R. Where B is referred to as the modulus.
#
# step counter-clockwise.)
#
# For example :
#
# 13 / 5 = 2 remainder 3
#
# 0 / 3 = 0  remainder  0
#
# 1 / 3 =  0 remainder   1
#
# 2 / 3 = 0  remainder  2
#
# 3 / 3  = 1 remainder   0
#
# 4 / 3 =  1 remainder   1
#
# 5 / 3 =  1  remainder  2
#
# 6 / 3  = 2 remainder   0
#
#
#
# The remainders start at 0 and increases by 1 each time, until the number reaches one less than the number we are dividing by. After that, the sequence repeats.
# """


#python control flow
# """
# comparison operators in python include
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equals to
# <= less than or equals to
# """
# loan = 70_000
# repayment = 50_000
#
# if loan > repayment:
#     print(f"You still owe me {loan - repayment}")
# else:
#     print("You have cleared your debt")
#
# balance = loan - repayment
# if balance == 0:
#     print("Your debt is clear")
# else:
#     print(f"You owe me {balance}")

# bill = 500
# if bill == 500:
#     print("Bill paid")
# else:
#     print("Pay up")

# bill = 500
# response = "yes"
# if response == "no":
#     print("User response is NO")
# else:
#     print("User response is YES")
# #The answer is yes because "YES" is different from "NO"
#
# bill = 500
# response = "yes"
# if response != "no":
#     print("User response is NO")
# else:
#     print("User response is YES")
# #The answer is ""NONO"" because the user response is not NO.
#
# loan = 500
# repayment = 450
#
# if loan <= repayment:
#     print("You ahve paid off your loan")
# else:
#     print("Pay up your money")
#
#
# #Indentation and IndentationError
# #conditional statement
# fee1 = 5000
# if fee1 >= 5000:
#     print("Access granted")
# else:
#     print("Access denied")
#
# fee2 = 2500
# if fee2 >= 5000:
#     print("Acess granted")
# else:
#     print("Access denied")
#
# fee3 = 2500
# if fee3 >= 5000:
#     print("Full Access granted")
# elif fee3 >= 2000:
#     print("Limited Access Granted")
# else:
#     print("Access Denied")

# while True:
#     my_sanity = int(input("On a scale of 1-10, how insane are you?\n"))
#     if my_sanity <= 7:
#         print("Keep it up")
#     elif my_sanity <= 5:
#         print("You probably should rethink this")
#     else:
#         print("Abort mission")
#     try_again = input("Do you want to try again? Answer with Yes or No \n").lower()
#     if try_again == "yes":
#         print(my_sanity)
#     elif try_again != "yes" or "no":
#         print("You entered the wrong command")
#     else:
#         break


# while True:
#     my_sanity = int(input("On a scale of 1-10, how insane are you?\n"))
#
#     # Check from highest threshold to lowest to avoid the bug
#     if my_sanity > 7:
#         # Scores 8, 9, 10
#         print("Abort mission")
#     elif my_sanity >= 5:
#         # Scores 5, 6, 7 (since >7 already filtered out)
#         print("Keep it up")
#     else:
#         # Scores 4, 3, 2, 1, and below
#         print("You probably should rethink this")
#
#     again = input("Evaluate again? (yes/no): ").lower()
#     if again != "yes":
#         break

# fruit = input("Which of the following fruits do you want to buy?\nApple, Cucumber, Orange, Watermelon, Grape, Lemon\n").lower()
# if fruit == "grape" or "apple":
#     print("The price is $5")
# elif fruit == "orange" or "lemon":
#     print("The price is $7")
# elif fruit == "watermelon" or "cucumber":
#     print("The price is $3")
# else:
#     print("We don't have their fruit in stock")
#
# score = int(input("What is your score over 100?\n"))
# if score > 100:
#     print("Try again. You entered an incorrect score")
# elif score >= 70:
#     print("Your score is excellent")
# elif score >= 60:
#     print("Your score is very good")
# elif score >= 50:
#     print("Your score is good")
# else:
#     print("You failed")

# #logical operators
# #and, or, not
# """
# Logical operators combines two conditions
# """
# #toilet managament system
# age = int(input("How old are you?\n"))
# gender = input("Are you male or female?\n").lower()
#
# if age >= 18 and gender == "male":
#     print("Use the male restroom by your right")
# elif age < 18 and gender == "male":
#     print("Go home little boy")
# elif age >= 18 and gender == "female":
#     print("Use the female restroom by your left")
# elif age < 18 and gender == "female":
#     print("Go home little girl")
# else:
#     print("Perhaps you entered the age or gender")

#the 'not' operator inverses booleans i.e. from true to false and false to true

# fruit = input("What fruit do you want?\nChoose one of the following: African Orange, American Orange, Apple, Banana, Grape, Guava\n").lower()
# if fruit == "orange":
#     orange_type = input("What type of orange do you want?\nAmerican Orange or African Orange\n").lower()
#     if orange_type == "american orange":
#         print("The price is $10")
#     elif orange_type == "african orange":
#         print("The price is $20")
#     else:
#         print("We don't have that in stock")
# elif fruit == "apple" or "grape" or "guava":
#     print("The price is $50")
# elif fruit == "banana":
#     print("The price is $5")
# else:
#     print("Out of stock. Please order what we have in stock")

# #number checker
# number = int(input("Enter a number\n"))
#
# #create a conditional statement
#
# if number == 0:
#     print("The number is zero")
# elif number > 0:
#     print("The number is positive")
# elif number < 0:
#     print("The number is negative")

# #nested if/else statement
# #outer or top conditional statement
# user_response = input("Are you hungery? Yes or No\n").lower()
# if user_response == "yes":
#     print("Go to the grocery store")
#     chocolate_price = float(input("How much is a bar of chococlate?\n"))
#     if chocolate_price <= 1:
#         print("I'd take 3 chocolate bars")
#     else:
#     # elif chocolate_price > 1:
#         print("I'd have just one chocolate bar")
#     #inner conditional statement
# elif user_response == "no":
#     print("Stay at home")
#     fortnite = input("Would you like to play FortNite? Yes or No\n").lower()
#     if fortnite == "yes":
#         print("Grab a controller")
#     elif fortnite == "no":
#         print("Its back to studying then")
#         subject = input("What is your favourite subject?\n").lower()
#         if subject.lower() in ("maths", "physics", "Geography", "Chemistry", "Further Maths",):
#             print("I'm a fan of solving stuffs as well")
#         else:
#             print("We have nothing in common")
#     else:
#         print("You need to make up your mind buddy")
# else:
#     print("Invalid response")

# #coding challenge
# # footbal administrator project
# match_status = input("What is the status of the match? Answer with any of the following options: Played or Suspended\n").lower()
# if match_status == "played":
#     home_goals = int(input("How many goals did the home team score?\n"))
#     away_goals = int(input("How many goals did the away team score?\n"))
#     if home_goals > away_goals:
#         print("The home team won")
#     elif home_goals < away_goals:
#         print("The away team won")
#     else:
#         print("It ended in a draw")
# elif match_status == "suspended":
#     print("The match was suspended")
# else:
#     print("Invalid match status")

# #coding challenge
# #minutes to hour converter
# converter = float(input("How many minutes will you luke to convert?\n"))
# # num_hours = converter/60
# # print(f"You have {num_hours} hours")
# minutes = converter % 60
# hours = converter // 60
# print(f"You have {hours} hours and {minutes} minutes")

#tenary operator
# [on_true] if [expression] else [on_false]

# a = 10
# b = 20
#
# min = a if a < b else b
# print(min)

language = input("What is your favouriate programming language?\n").lower()
if language == "python" : print("Great!") #else: print("Go to hell")
skin = input("What is your skin colour?\n").lower()
race = "African" if skin =="black" else "white"
print(race)