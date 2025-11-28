################################# responsible for checking user input and reading files #################################

import os
import json

def ask_text(message:str)->str:
    """
    Ask the user for a text input with optional validation.

    Args:
        message (str): The message to display to the user.

    Returns:
        str: The input text 
    """

    text = input(message)
    # Check if the user entered an empty string or a string of whitespace characters
    if  text == '' or text.isspace():
        return ask_text(f"{message}")
    # Remove leading and trailing whitespace characters
    res = text.strip()
    return res

#print(ask_text('test'))

def ask_number(message:str,min_val:int,max_val:int)->int:
    """
    Ask the user for a number with optional bounds.

    Args:
        message (str): The message to display to the user.
        min_val (int, optional): The minimum value for the number. Defaults to None.
        max_val (int, optional): The maximum value for the number. Defaults to None.

    Returns:
        int: The input number
    """

    # Ask the user for a number
    number_str = input(message)

    try:
        # Try to convert the input to an integer
        number = int(number_str)
    except ValueError:
        # If the input is not an integer, print an error message and ask again
        print(f"Please enter a integer")
        return ask_number(message,min_val,max_val)

    # Check if the number is within the bounds
    if min_val is None and max_val is None:
        # If there are no bounds, return the number
        return number

    elif min_val is None:
        # If there is no minimum bound, check if the number is lower than the maximum bound
        if number > max_val:
            # If the number is greater than the maximum bound, print an error message and ask again
            print(f"Please enter a number lower than {max_val}.")
            return ask_number(message,min_val,max_val)
        # If the number is within the bounds, return it
        return number

    elif max_val is None:
        # If there is no maximum bound, check if the number is greater than the minimum bound
        if number < min_val:
            # If the number is lower than the minimum bound, print an error message and ask again
            print(f"Please enter a number greater than {min_val}.")
            return ask_number(message,min_val,max_val)
        # If the number is within the bounds, return it
        return number

    else:
        # If there are both minimum and maximum bounds, check if the number is within them
        if number < min_val or number > max_val:
            # If the number is not within the bounds, print an error message and ask again
            print(f"Please enter a number between {min_val} and {max_val}.")
            return ask_number(message,min_val,max_val)
        # If the number is within the bounds, return it
        return number

#print(ask_number("Enter a number between 1 and 10: ",1,10))

def ask_choice(message: str, options: list) -> str:
    """
    Ask the user to make a choice from a list of options.

    Args:
        message (str): The message to display to the user.
        options (list): The list of options to choose from.

    Returns:
        str: The chosen option.
    """

    print(message)

    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    choice_str = input("Your choice: ")

    try:
        # Try to convert the input to an integer
        choice = int(choice_str)
    except ValueError:
        # If the input is not an integer, print an error message and ask again
        print(f"Please enter the number and not the text")
        return ask_choice(message, options)

    # Check if the number is within the bounds
    if choice < 1 or choice > len(options):
        print(f"Please enter a choice between 1 and {len(options)}")
        return ask_choice(message, options)

    # If the number is within the bounds, return the chosen option
    return options[choice - 1]

"""
choices = ["Yes","No","JSPA"]
message = "Quelle est la capitale de la France" 
print(ask_choice(message,choices))
"""


def load_file(file_path:str)->dict:
    """
    Load a JSON file from a given path.

    Args:
        file_path (str): The path to the JSON file to load.

    Returns:
        dict: The loaded JSON data, or an error message if the file does not exist.
    """

    # Check if the file exists at the given path.
    if not os.path.isfile(file_path): 
        return {"error": "Chemin n'existe pas"}

    # Open the file and load the JSON data.
    with open(file_path,'r') as f1:
        return json.load(f1)
    
