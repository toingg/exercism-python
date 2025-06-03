"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# TODO_DONE: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO_DONE: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time

    return time_remaining 

#TODO_DONE: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes

    :param number_of_layers: int - how many layer * PREPARATION_TIME or 2 minutes
    :return: int - preparation time total (in minutes)
    """

    return number_of_layers * PREPARATION_TIME 



#TODO_DONE: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate total elapsed time in minutes

    :param 
    number_of_layers: int - how many layer * PREPARATION_TIME [so i called the function inside this function]
    elapsed_bake_time: int - minutes of elapsed bake time in oven
    :return: int - elapsed time in total
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


# TODO_DONE: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
