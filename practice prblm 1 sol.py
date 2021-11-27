# PROBLEM TOPIC
"""
your age in 2090

take year or age or birth as an input from the user and tell them when they will turn
100 yaers old. (do not use any type of module , like datetime or dateutils)
they can then optionally provide a yaer and your program must tell their age in that particular year.

you should be handeling all sorts of errors like:
you are not yet born
ypu seem to be older person alive
you can also handle any other error if possible!


Author: Siddhesh
Date: 21 Nov 2021
Purpose: Practice problem
"""

yearAge = int(input("What is your Age/Year of birth \n"))
isAge = False
isyear = False
if len(str(yearAge)) == 4:
    isYear = True



else:
    isAge = True

if yearAge < 1900 and isyear:
    print("You seem to be oldest person alive")
    exit()

if yearAge > 2021:
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2021 - yearAge

print(f"You will be 50 years old in {yearAge + 50}")

interestedYear = int(input("Enter the year you want to know in \n"))
print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")