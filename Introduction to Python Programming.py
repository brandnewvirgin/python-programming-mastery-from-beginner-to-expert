# course_title = "Python Programming Master"
# title2 = "PPM"
# advanced_course_2 = "Django Course"
# new_line = "I am a text on a new line"
# #&symbol = "Symbol
#
# #string manipulation
# #string concatenation
# complete_course = course_title + " " + title2 + "\n" + new_line
# #seperator = course_title - title2
# print(complete_course)
# #print(seperator)
#
# name = "Phillip"
# age = 19
# role = "Python engineer and instructor"
#
# #f string
# # info = "My name is " + name + ". I'm a " + age + " years old " + role
# # print(info)
# info_f_string = f"My name is {name}. I'm a {age} years old {role}"
# print(info_f_string)
#
# """
# docstring
# docstring is used to make multiline comments
# docstring is done with three single or double quotes
# # ctrl + / or command + / is used for making comments
# # goes before the comments
# """

# python_inventor = "Guido van rossum"
# integer = 90
# type_of_integer = type(integer)
# print(type_of_integer)
# python_inventor = "Guido van rossum"
# integer_2 = 19_000
# type_of_integer_2 = type(integer_2)
# print(type_of_integer_2)
# '''
# type function in python is used in checking the type of an object
# an argument is actual value passed to the function when called and it is stored in a ()
# integer is a whole number without a decimal point
# string is any letter or number encased in double or single quotes
# float is a fractional number with decimal places
# boolean is a statement requiring true or false answers
# '''
# python_inventor = "Guido van rossum"
# bill = 9.0
# type_of_bill = type(bill)
# print(type_of_bill)
# python_inventor = "Guido van rossum"
# date = "90"
# type_of_date = type(date)
# print(type_of_date)

#data type conversion / python casting / data type casting
#it involves converting data from one type to another i.e. from string to integer, string to float or integer to float

# twitter_ceo = "Elon Musk"
# twitter_worth = "7_000_000_000"
# age = 18
# cost = 1945.77
# is_rich = True

# data_type = type(twitter_worth)
# print(data_type)
#
# #conversion of string to integer
# int_musk = int(twitter_worth)
# print(int_musk)
# str_age = str(age)
# int_age = int(age)
# str_cost = str(cost)
# int_cost = int(cost)
# print(str_age)
# print(int_age)
# print(str_cost)
# print(int_cost)
# print(type(str_age))
# print(type(int_age))
# print(type(str_cost))
# print(type(int_cost))
# str_is_rich = str(is_rich)
# print(str_is_rich)
# print(type(str_is_rich))

#converting strings to boolean data is complicated


# #input function
#
# prog_lang = input("What is your favourite programming language? ")
# print(prog_lang)
# print(type(prog_lang))
#
# age = input("How old are you?\n")
# print(age)
# print(type(age))
# age_int = int(age)
# print(age_int)
# print(type(age_int))
#
# feedback = input("This is a great Python course. True or false? ")
# print(feedback)
# print(type(feedback))

#coding challenge my dream job
my_name = input("What is your name?\n")
dream_company = input("What is your dream company?\n")
prom_lang = input("What is your favourite programming language?\n")
description = "My name is " + my_name + ". I hope to work at " + dream_company + " as a " + prom_lang + " programmer in the future"
f_description = f"My name is {my_name}. I hope to work at {dream_company} as a {prom_lang} programmer in the future"
print(description)
print(f_description)