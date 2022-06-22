#############################################################################################
# File Name: generate.py                                                                    #
# Python Version: 3.9.13                                                                    #
#                                                                                           #
# Author: Bryce Whitney                                                                     #
# Last Edit: June 22, 2022                                                                  #
#                                                                                           #
# Combines randomPassword.py and interface.py to generate a password                        # 
# of the user's specification                                                               #
#############################################################################################

# Required imports
from interface import generateInterface
from randomPassword import generatePassword
import argparse
import os

# Run the program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates a random password using letters (uppercase and lowercase), numbers, and symbols.")
    
    # Add command line arguments
    # Command line vs GUI argument - GUI by Default
    parser.add_argument("-t", "--terminal", action=argparse.BooleanOptionalAction,
                        help="Runs in the terminal if -t is passed, otherwise opens the GUI")
    
    # Length and Seed arguments
    parser.add_argument("-l", "--length", default=8, type=int,
                   help="Desired password length, 8 characters by deafult")
    parser.add_argument("-r", "--randomSeed", default=None, type=int,
                   help="Desired random seed, None by deafult")
    
    # Read any commandline arguements sent to the program
    # NOTE: if -h or --help, the program stops here
    args = parser.parse_args()

    # If terminal flag, generate password directly. otherwise open ther GUI
    if(args.terminal):
        password = generatePassword(passwordLength=args.length, randomSeed=args.randomSeed)
        
        # Copy the password to the clipboard
        os.system(f"echo {password.strip()}| clip")
        
        # Print the password
        print(password)
    else:
        generateInterface()