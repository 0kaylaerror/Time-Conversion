"""
time_conversion.py

This module contains functions that convert a number of seconds
into various non-conventional time units.

Each function accepts an integer number of seconds
and returns the converted value.
"""

def decaseconds_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to decaseconds.
        1 decasecond = 10 seconds.

    Output:
        Return the equivalent number of decaseconds.
    """
    decasecond_conv = round((seconds / 10),2)
    print(float(decasecond_conv) , "Decaseconds")

    return float(decasecond_conv)



def jiffies_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to jiffies.
        1 jiffy = 10 milliseconds.

    Output:
        Return the equivalent number of jiffies.
    """

    milliseconds = seconds * 1000
    jiffy_conversion = (milliseconds / 10)
    return float(jiffy_conversion)


def new_york_minutes_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to New York Minutes.
        1 New York Minute = 1/20 of a second

    Output:
        Return the equivalent number of New York Minutes.
    """

    New_york_minute = round(seconds / (1/20),2)
    print((New_york_minute) , "New york minutes")
    return float(New_york_minute)

def nanocenturies_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to Nanocenturies.
         1 Nanocentury = 3.156 seconds

    Output:
        Return the equivalent number of Nanocenturies.
    """

    Nanocentury = (seconds / 3.156)
    
    print((Nanocentury), "Nanocenturies")
    return float(Nanocentury)


def snapchat_streak_days_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to Snapchat Streak Days.
        1 Snapchat Streak Day = 24 hours

    Output:
        Return the equivalent number of Snapchat Streak Days.
    """

    Snapchat_streak = (seconds / 86400)
    ''' There are 86400 seconds in 24 hours'''
    float(Snapchat_streak)
    print(Snapchat_streak , "Snapchat streak days")
    return float(Snapchat_streak)

def custom_time_conversion(seconds:float)->float: 
    
    '''
    Input: 
    seconds (int): A number of seconds

    Process: 
    Convert the number of seconds to Hironos. 
    1 Hirono = 4.523 seconds

    Output: 
    Return the equivalent number of Hironos
    '''

    hirono_conversions = (seconds / 4.523)
    print(seconds ,"seconds will reward you with", hirono_conversions, "Hironos!")
    return float(hirono_conversions)
