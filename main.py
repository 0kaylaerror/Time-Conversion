"""
main.py

Driver program for the Time Conversion project.
Prompts the user for a number of seconds and
displays time conversions using the time_conversion module.
"""

# import the module
import time_conversion

# TO DO #1: Declare a variable called num_seconds and assign it a value of 0
# add your code here
num_seconds = 0

def main():

    # statements for output formatting
    print("*******************************")
    print("Start - Time Conversion Program")
    print("*******************************")

    
    # TO DO #2: ask the user to enter the number of seconds to be converted
    # and assign the value to num_seconds as an integer value
    # add your code here
    global num_seconds
    num_seconds = int(input("Enter a whole number of seconds: "))



    #####################################################
    # you do not need to add anything below this line

    # call function to calculate Decaseconds
    print(time_conversion.decaseconds_conversion(num_seconds))

    # call function to calculate Jiffies
    print(time_conversion.jiffies_conversion(num_seconds))

    # call function to calculate New York Minutes
    print(time_conversion.new_york_minutes_conversion(num_seconds))

    # call function to calculate Nanocenturies
    print(time_conversion.nanocenturies_conversion(num_seconds))

    # call function to calculate Snapchat Streak Days
    print(time_conversion.snapchat_streak_days_conversion(num_seconds))

    # uncomment the function call to calculate custom time
    print(time_conversion.custom_time_conversion(num_seconds))

    # statements for output formatting
    print("*******************************")
    print("End - Time Conversion Program")
    print("*******************************")


if __name__ == "__main__":
    main()

# Reflection;
# When running my test I used integers and floats as my values. 
# I verified my calculations were correct by double checking with google. 
# The outputs make sense given the inputs because the process was done completely 
# following the rules given, so the outputs just went through the process making 
# their outputs true. I would say making my custom_conversion was easy because I 
# practiced and had time to go through time and error so the custom was stright 
# forward. The challenging thing was putting a function into a functio I forgot 
# how to do that. but also the 24hr conversion as I wasn't reading correctly & 
# if I didn't double-check it would've been wrong.