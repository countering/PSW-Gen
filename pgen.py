# simple code

import random
import string
import os

import colorama
from colorama import Fore, Back


SETTINGS_FILE = "password_settings.txt"


settings = {
    'lowercase': False,
    'uppercase': False,
    'digits': False,
    'symbols': False
}

def save_settings():
    with open(SETTINGS_FILE, 'w') as f:
        for key, value in settings.items():
            f.write(f"{key}:{value}\n")

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                settings[key] = True if value == 'True' else False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_password(length=12):
    characters = ''
    if settings['lowercase']:
        characters += string.ascii_lowercase
    if settings['uppercase']:
        characters += string.ascii_uppercase
    if settings['digits']:
        characters += string.digits
    if settings['symbols']:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def print_menu():
    clear_screen()
    print(Fore.BLUE + '''
 ________  ________  ________  _______   ________      
|\   __  \|\   ____\|\   ____\|\  ___ \ |\   ___  \    
\ \  \|\  \ \  \___|\ \  \___|\ \   __/|\ \  \\ \  \   
 \ \   ____\ \_____  \ \  \  __\ \  \_|/_\ \  \\ \  \  
  \ \  \___|\|____|\  \ \  \|\  \ \  \_|\ \ \  \\ \  \ 
   \ \__\     ____\_\  \ \_______\ \_______\ \__\\ \__]
    \|__|    |\_________\|_______|\|_______|\|__| \|__|
             \|_________|''')
    print(" ")
    print(Back.BLUE + Fore.WHITE + "Type number to select, type it again to unselect. You are able to select multiple settings.")
    print(Back.BLACK + " ")
    print(Fore.WHITE +"[1] Lowercase:", "ON" if settings['lowercase'] else "OFF")
    print("[2] Uppercase:", "ON" if settings['uppercase'] else "OFF")
    print("[3] Digits:", "ON" if settings['digits'] else "OFF")
    print("[4] Symbols:", "ON" if settings['symbols'] else "OFF")
    print("[5] Generate")
    print("[6] Quit")

def main():
    load_settings()
    while True:
        print_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            settings['lowercase'] = not settings['lowercase']
        elif choice == '2':
            settings['uppercase'] = not settings['uppercase']
        elif choice == '3':
            settings['digits'] = not settings['digits']
        elif choice == '4':
            settings['symbols'] = not settings['symbols']
        elif choice == '5':
            password = generate_random_password()
            clear_screen()
            print("Generated password:", password)
            input("Press Enter to continue...")
        elif choice == '6':
            save_settings()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
