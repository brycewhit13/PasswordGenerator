#############################################################################################
# File Name: interface.py                                                                   #
# Python Version: 3.9.13                                                                    #
#                                                                                           #
# Author: Bryce Whitney                                                                     #
# Last Edit: June 22, 2022                                                                  #
#                                                                                           #
# Generates the interface associated with randomPassword.py                                 #
#############################################################################################

# Required imports
import os
import random
from randomPassword import generatePassword
import tkinter as tk
from tkinter import messagebox

###################
# Constant Fields #
###################
MIN__PASS_LENGTH = 0
MAX_PASS_LENGTH = 50
MIN_SEED = 0
MAX_SEED = 4_000_000
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 350

# Padding Widths
SHORT_PAD_X = 50
HORIZONTAL_WIDGET_SPACING = 150

# Fonts
REGULAR_FONT=14
LARGE_FONT = 16
TITLE_FONT=30

def generateInterface():
    """ 
    Generates the GUI for the user to generate their random password. They can select whether or not to include capital letters, lowercase letters, 
    numbers, and symbols in the password. At least one of the sets is required to be included. The user can specify the length of the password and random seed 
    to use for generation, allowing them to regenerate any passwords they may have forgotten.  
    """

    ########################
    # Validation Functions #
    ########################
    def cb_check():
        """
        Checks to ensure at least one of the check buttons is always checked. If only 1 is selected, it disables that check button until another one is checked. 
        If there are more than 1 checked, then all the buttons remain active. 
        """
        # Booleans to see which buttons are checked
        capsChecked = includeCapitals.get()
        lowersChecked = includeLowers.get()
        numsChecked = includeNumbers.get()
        symbolsChecked = includeSymbols.get()

        # Check if three of them are unchecked
        # True = 1 and False = 0 when adding booleans
        if(capsChecked + lowersChecked + numsChecked + symbolsChecked == 1):
            # Disable the only one that is checked to ensure a password can still be generated
            if(capsChecked): capButton.config(state="disabled")
            elif(lowersChecked): lowButton.config(state="disabled")
            elif(numsChecked): numButton.config(state="disabled")
            else: symbolButton.config(state='disabled')

        # Otherwise ensure they are all enabled again
        # Use list comprehesion to keep it compact
        else: [button.config(state='normal') for button in [capButton, lowButton, numButton, symbolButton]]

    def pass_length_check(length):
        # Ensure a number is passed for the length
        valid = (length.isdigit() and int(length) >= MIN__PASS_LENGTH and int(length) <= MAX_PASS_LENGTH) or (length == '')
        return valid
    
    def rand_seed_check(seed):
        # Ensure a valid random seed is passed
        valid = (seed.isdigit() and int(seed) >= MIN_SEED and int(seed) <= MAX_SEED) or (seed == '')
        return valid

    ######################
    # Save Functionality #
    ######################
    def save_password(file_loc="passwords.csv", application='', password='', length=0, seed=0, savePass=True):
        """Saves the password to the file provided. has the option to only save the length and seed if the user
        doesn't want to save the password itself.

        Args:
            file_loc (str, optional): Location to the save file. Should be a CSV file. Defaults to 'passwords.csv'. 
            application (str, optional): Website the password will be used for. Defaults to ''.
            password (str, optional): The generated password. Defaults to ''.
            length (int, optional): Length of the generated password. Defaults to 0.
            seed (int, optional): Random seed that was used for generation. Defaults to 0.
            savePass (bool, optional): Saves the password if True, otherwise only saves the length 
                                        and seed so it can be generated again. Defaults to True.
        """
        # Check that a csv was passed
        if(file_loc.endswith('.csv') == False):
            messagebox.showerror("Invalid Path", f"Please enter a path to a CSV file, the following is not a valid path:\n \"{file_loc}\"")
            return
            
        # Chceck if the file exists already
        if(os.path.exists(file_loc)):
            # Append the information to the file
            with open(file_loc, 'a') as file:
                if(savePass):
                    file.write(f"{application},{password},{str(length)},{str(seed)}\n")
                else:
                    file.write(f"{application},' ',{str(length)},{str(seed)}\n")
        
        # If it doesn't exist, create the file and add headers to the top 
        else:
            with open(file_loc, 'w') as file:
                # Generate headers for new file
                file.write("Application,Password,Length,Random Seed\n")
                # Append password information
                if(savePass):
                    file.write(f"{application},{password},{str(length)},{str(seed)}\n")
                else:
                    file.write(f"{application},' ',{str(length)},{str(seed)}\n")
        
        # Success Message
        messagebox.showinfo("Successful Save", f"Information successfully saved to {file_loc}")
        
        
    ##################
    # Create the GUI #
    ##################
    window = tk.Tk()
    window.title("Random Password Generator")
    window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}') # Window size

    validate_pass_length = (window.register(pass_length_check), '%P')
    validate_seed = (window.register(rand_seed_check), '%P')

    # Title
    title = tk.Label(window, text="Random Password Generator", font=("Times", TITLE_FONT, 'bold'))
    title.grid(row=0, columns=1, columnspan=2, padx=SHORT_PAD_X + 50, sticky='w')

    ###########################################################################
    # CheckButtons for what characters can be included in the password        #
    ###########################################################################
    # Label for check buttons
    l1 = tk.Label(window, text="Characters to Include:", font=("Times", REGULAR_FONT, "bold"))
    l1.grid(row=1, column=0, sticky='e')
    
    # Initialize variables for check buttons
    includeCapitals = tk.BooleanVar()
    includeLowers = tk.BooleanVar()
    includeNumbers = tk.BooleanVar()
    includeSymbols = tk.BooleanVar()

    # Create checkbuttons
    capButton = tk.Checkbutton(window, text="Capital Letters", variable=includeCapitals, offvalue=False, onvalue=True,
                            command=cb_check)
    capButton.select() # Start checked by default
    capButton.grid(row=1, column=1, sticky='w', padx=SHORT_PAD_X)

    lowButton = tk.Checkbutton(window, text='Lowercase Letters', variable=includeLowers, offvalue=False, onvalue=True,
                            command=cb_check)
    lowButton.select()
    lowButton.grid(row=1, column=1, sticky='w', padx=SHORT_PAD_X + HORIZONTAL_WIDGET_SPACING)

    numButton = tk.Checkbutton(window, text='Numbers', variable=includeNumbers, offvalue=False, onvalue=True,
                            command=cb_check)
    numButton.select()
    numButton.grid(row=2, column=1, sticky='w', padx=SHORT_PAD_X)

    symbolButton = tk.Checkbutton(window, text='Symbols', variable=includeSymbols, offvalue=False, onvalue=True, 
                                command=cb_check)
    symbolButton.select()
    symbolButton.grid(row=2, column=1, sticky='w', padx=SHORT_PAD_X + HORIZONTAL_WIDGET_SPACING)

    #####################################################
    # Create fields for password length and random seed #
    #####################################################
    # Labels for Password and Seed
    l2 = tk.Label(window, text=f"Password Length ({MIN__PASS_LENGTH}-{MAX_PASS_LENGTH}):", font=("Times", REGULAR_FONT, "bold"))
    l2.grid(row=3, column=0, sticky='e')
    l3 = tk.Label(window, text=f"Random Seed ({MIN_SEED}-{int(MAX_SEED / 1_000_000)} Mil):", font=("Times", REGULAR_FONT, "bold"))
    l3.grid(row=4, column=0, sticky='e')
    
    # Initialize variables for password length and random seed
    passwordLength = tk.StringVar()
    randomSeed = tk.StringVar()

    # Create Entry's
    passEntry = tk.Spinbox(window, from_=MIN__PASS_LENGTH, to=MAX_PASS_LENGTH, textvariable=passwordLength, wrap=True, 
                            validate = 'all', validatecommand=validate_pass_length)
    passwordLength.set("8") # Default value
    passEntry.grid(row=3, column=1, padx=SHORT_PAD_X, sticky='w')

    randseedEntry = tk.Spinbox(window, from_=MIN_SEED, to=MAX_SEED, textvariable=randomSeed, 
                            validate = 'key', validatecommand=validate_seed)
    randomSeed.set(random.choice(range(MIN_SEED, MAX_SEED)))
    randseedEntry.grid(row=4, column=1, padx=SHORT_PAD_X, sticky='w')
    
    def randomizeSeed():
        """ Helper function and button to facilitate changing the random seed randomly """
        randomSeed.set(random.choice(range(MIN_SEED, MAX_SEED)))
    
    randomizeButton = tk.Button(window, text="Randomize Seed", command=randomizeSeed)
    randomizeButton.grid(row=4, column=1, sticky='w', padx=SHORT_PAD_X + HORIZONTAL_WIDGET_SPACING)

    ###############################
    # Fields to Save the Password #
    ###############################
    save_file_path = tk.StringVar()
    application_description = tk.StringVar()
    
    # Application Description
    l5 = tk.Label(window, text="Website (Optional for Saving):", font=("Times", REGULAR_FONT, "bold"))
    l5.grid(row=5, column=0, sticky='e')
    
    appDescription = tk.Entry(window, textvariable=application_description, width=70)
    application_description.set("")
    appDescription.grid(row=5, column=1, padx=SHORT_PAD_X, sticky='w')
    
    # File location Entry
    l6 = tk.Label(window, text="Save Location (CSV):", font=("Times", REGULAR_FONT, "bold"))
    l6.grid(row=6, column=0, sticky='e')
    
    saveLocation = tk.Entry(window, textvariable=save_file_path, width=70)
    save_file_path.set(os.path.join(os.getcwd(), "passwords.csv"))
    saveLocation.grid(row=6, column=1, padx=SHORT_PAD_X, sticky='w')
    
    # Create Save Button
    saveButton = tk.Button(window, text="Save Password", font=("Times", LARGE_FONT),
                           command=lambda: save_password(save_file_path.get(), application_description.get(), generatedPassword.get(), 
                                                         int(passwordLength.get()), int(randomSeed.get()), savePass=True))
    saveButton.grid(row=8, column=1, padx=SHORT_PAD_X + HORIZONTAL_WIDGET_SPACING + 50, pady=20, sticky='w')
    
    #########################################
    # Button and Entry to Generate Password #
    #########################################
    generatedPassword = tk.StringVar() # Variable for Button to track
    
    # Label
    l4 = tk.Label(window, text="Password:", font=("Times", REGULAR_FONT, "bold"))
    l4.grid(row=7, column=0, sticky='e')
    
    # Entry to hold generated password
    generatedPasswordEntry = tk.Entry(window, textvariable=generatedPassword, width=(MAX_PASS_LENGTH + 5), font=("Times", LARGE_FONT))
    generatedPasswordEntry.grid(row=7, column=1, padx=SHORT_PAD_X, sticky='w')

    def generate():
        """ Function to check fields and actually generate the password """
        # Check that a length and seed are entered
        if(passwordLength.get() == ''):
            passwordLength.set(0)
        if(randomSeed.get() == ''):
            randomSeed.set(0)
        # Generate the password
        generatedPassword.set(generatePassword(int(passwordLength.get()), int(randomSeed.get()), includeCapitals.get(), 
                                                                       includeLowers.get(), includeNumbers.get(), includeSymbols.get()))
    
    # Create Generation Button
    generateButton = tk.Button(window, text="Generate Password", font=("Times", LARGE_FONT), command=generate)
    generateButton.grid(row=8, column=1, padx=SHORT_PAD_X, sticky='w')

    #####################
    # Run the eventloop #
    #####################
    window.mainloop()