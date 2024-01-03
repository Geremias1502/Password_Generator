import random
import string
import sys

def main():
    prompt = get_input(input("Do you want to generate a password? "))
    print("\n" + "Password: " + generate_password(check_length(get_password_length(prompt))))

def get_input(prompt: str):
    """
    Checks if the input given is yes or no. Exits if anything else from a yes is given.
    """
    prompt = prompt.lower()
    # Checks if the user wants to generate a password
    if prompt == "y" or "yes" or "yeah":
        return prompt
    else:
        sys.exit("You didn't say 'yes'")

def get_password_length(_):
    """
    Returns the length of the password, once the user said yes
    """
    print("(Mind that the minimum amount of characters is 8)")
    return input("How long do you want your password to be? ")

def check_length(length: str):
    """
    Checks if the argument given is a number and catches any ValueErrors.
    """
    try:
        # Is length variable a number
        if length.isnumeric():
            pass

        length = int(length)

        # The input does not meet the minimum required
        if length < 8:
            sys.exit("Input a value equal or greater than 8.")

        # The input given passes all the requirements
        else:
            return length

    # Checks for ValueError
    except ValueError:
        exit("You should input a whole number, not a word or written number.")

def generate_password(length: int):
    """
    Generates the password for the user based on the length given
    """
    # Establishes the characters to be used in a list
    password_chars = [string.ascii_letters + string.punctuation + string.digits]

    # Loops through the password_chars[] and passes it to chars[]
    # from password_chars['abcdefgh12345.?=:...'] --> chars['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',...]
    chars = [chars for chars in password_chars[0]]

    # Shuffles the elements in the list twice to guarantee the creation of a new combination of password
    random.shuffle(chars)
    random.shuffle(chars)

    # Chooses the random characters for the creation of the password
    password = [random.choice(chars) for _ in range(length)]

    # Joins all the elements of the list to create a string
    password = "".join(password)

    return password

if __name__ == "__main__":
    main()