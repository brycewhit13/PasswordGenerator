#############################################################################################
# File Name: randomPassword.py                                                              #
# Python Version: 3.8.10                                                                    #
#                                                                                           #
# Author: Bryce Whitney                                                                     #
# Last Edit: May 13, 2022                                                                   #
#                                                                                           #
# Generates a random password using letters (uppercase and lowercase), numbers, and symbols #
#############################################################################################

# Required Imports
import string
import random

def generatePassword(passwordLength=10, randomSeed=None, includeUppercase = True, includeLowercase = True, includeNumbers = True, includeSymbols = True):
    """
    Generates a random password of the length provided in the command line. If no length is given, the default is 10 characters. 
    The user can also pass a random seed argument so they can reproduce their results. This way they can track the seeds they used
    in a seperate file and regenerate their password when they forget it. 

    Arguments:
        passwordLength [int] -- Length of the desired password. 10 characters by deafult. 
        randomSeed     [int] -- The random seed to be used. None by deafult.
    """

    # Initialize character set
    CHARACTERS = ''

    # Create set of characters based on parameters
    if(includeUppercase):
        CHARACTERS += string.ascii_uppercase
    if(includeLowercase):
        CHARACTERS += string.ascii_lowercase
    if(includeNumbers):
        CHARACTERS += string.digits
    if(includeSymbols):
        CHARACTERS += string.punctuation

    # Set the random seed
    random.seed(randomSeed)

    # Generate the password by sampling all characters and return it
    password = ''.join(random.choices(CHARACTERS, k=passwordLength))
    return password



'''
###############
# Main Method #
###############
if __name__ == '__main__':
    import argpare
    # Create an ArgumentParser class object for dealing with commandline args
    p = argparse.ArgumentParser(
        description="Generates a random password using letters (uppercase and lowercase), numbers, and symbols.")

    # Add an additional optional argument for the password length and random seed
    p.add_argument("-l", "--length", default=10, type=int,
                   help="Desired password length, 10 characters by deafult")
    p.add_argument("-r", "--randomSeed", default=None, type=int,
                   help="Desired random seed, None by deafult")

    # Read any commandline arguements sent to the program
    # NOTE: if -h or --help, the program stops here
    args = p.parse_args()

    # Generate and print the random password
    print(generatePassword(args.length, args.randomSeed))
'''