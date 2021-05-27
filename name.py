# This program takes first name and last name as input and print them in reverse order.

def input_firstname():
    first_name = input("Enter your first name: ")
    return first_name


def input_lastname():
    last_name = input("Enter your last name: ")
    return last_name


def print_reversed_name():
    firstname = input_firstname()
    lastname = input_lastname()
    print("Your name in reverse oder is: ", lastname, firstname)


print_reversed_name()
