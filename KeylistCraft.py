#!/usr/bin/env python3

import itertools
import os


#KeylistCraft Crafted by Avnish Singh


print('''\033[40m
     ##:::'##:'########:'##:::'##:'##:::::::'####::'######::'########::'######::'########:::::'###::::'########:'########:
    ##::'##:: ##.....::. ##:'##:: ##:::::::. ##::'##... ##:... ##..::'##... ##: ##.... ##:::'## ##::: ##.....::... ##..::
   ##:'##::: ##::::::::. ####::: ##:::::::: ##:: ##:::..::::: ##:::: ##:::..:: ##:::: ##::'##:. ##:: ##:::::::::: ##::::
   #####:::: ######:::::. ##:::: ##:::::::: ##::. ######::::: ##:::: ##::::::: ########::'##:::. ##: ######:::::: ##::::
   ##. ##::: ##...::::::: ##:::: ##:::::::: ##:::..... ##:::: ##:::: ##::::::: ##.. ##::: #########: ##...::::::: ##::::
   ##:. ##:: ##:::::::::: ##:::: ##:::::::: ##::'##::: ##:::: ##:::: ##::: ##: ##::. ##:: ##.... ##: ##:::::::::: ##::::
   ##::. ##: ########:::: ##:::: ########:'####:. ######::::: ##::::. ######:: ##:::. ##: ##:::: ##: ##:::::::::: ##::::
   ..::::..::........:::::..:::::........::....:::......::::::..::::::......:::..:::::..::..:::::..::..:::::::::::..:::::

\033[0m
''')

def generate_passwords():
    """
    Generate all possible passwords based on user input.
    """
    print("\033[1;32;40mWelcome! Please enter an alphabet, number, or symbol. Don't use comma to separate words, just type the words:\033[0m")
    user_input = input()
    
    # Generate all possible combinations of the user input
    passwords = [''.join(p) for p in itertools.product(user_input, repeat=len(user_input))]
    
    return passwords

def save_passwords(passwords, location):
    """
    Save passwords to a file provided by the user.
    If the file already exists, increment the filename.
    """
    with open(location, 'w') as file:
        for password in passwords:
            file.write(f"{password}\n")
        
    print(f"\033[1;34;40mPasswords saved to {location}\033[0m")

def main():
    passwords = generate_passwords()
    
    print("\033[1;33;40mTo see Keylist in terminal: \033[1;35;40mT\033[0m")
    print("\033[1;33;40mTo save in file:   \033[1;35;40mF\033[0m")

    choice = input()
    
    if choice.lower() == 't':
        for password in passwords:
            print(password)
    else:
        if choice.lower() == 'f':
            documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')
            if os.path.exists(documents_dir):
                save_dir = documents_dir
            else:
                save_dir = os.path.expanduser('~')  # Save directly in the user's home directory
            
            filename = 'Keylist'
            count = 0
            while os.path.exists(os.path.join(save_dir, f"{filename}{count}.txt")):
                count += 1
            filename = f"{filename}{count}.txt"
            
            location = os.path.join(save_dir, filename)
            save_passwords(passwords, location)
        else:
            print("\033[1;31;40mNo passwords will be saved.\033[0m")


if __name__ == "__main__":
    main()

print("\033[1;36;40mThanks for using KeylistCraft\033[0m")
