import string
import random
import math

def name():
    print("""                              WELCOME TO                                                   
           #######   ##    ####   ####  #    #  ####  #####  #####  
           #     #  #  #  #      #      #    # #    # #    # #    # 
           ######  #    #  ####   ####  #    # #    # #    # #    # 
           #       ######      #      # # ## # #    # #####  #    # 
           #       #    # #    # #    # ##  ## #    # #   #  #    # 
           #       #    #  ####   ####  #    #  ####  #    # #####  
                                                                    
             #####                                                 
            #     # ##### #####  ###### #    #  ####  ##### #    # 
            #         #   #    # #      ##   # #    #   #   #    # 
             #####    #   #    # #####  # #  # #        #   ###### 
                  #   #   #####  #      #  # # #  ###   #   #    # 
            #     #   #   #   #  #      #   ## #    #   #   #    # 
             #####    #   #    # ###### #    #  ####    #   #    # 
                                                                   
                #####                                            
               #     # #    # ######  ####  #    # ###### #####  
               #       #    # #      #    # #   #  #      #    # 
               #       ###### #####  #      ####   #####  #    # 
               #       #    # #      #      #  #   #      #####  
               #     # #    # #      #    # #   #  #      #   #  
                #####  #    # ######  ####  #    # ###### #    # 
 
 Created by Thaher Migdadi & Kasem Tawalbeh & Baker Sharadqah""")
    print()

def check_password_strength(password):
    with open('wordlist.txt', 'r') as wordlist_file:
        common_passwords = wordlist_file.read().splitlines()

    if password in common_passwords:
        return "Weak (Common Password)"
    
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if has_lower and has_upper and has_digit and has_symbol:
        return "Strong"
    elif has_lower and has_upper and has_digit:
        return "Moderate (No Special Character)"
    else:
        return "Weak (Doesn't Meet Criteria)"

def estimate_crack_time(password, complexity):
    # Adjust these values based on your own estimations
    guesses_per_second = 1000000000  # Number of guesses per second
    seconds_per_minute = 60
    minutes_per_hour = 60

    password_length = len(password)
    character_set_size = get_character_set_size(complexity)

    # Calculate total possible combinations
    total_combinations = character_set_size ** password_length

    # Calculate time to crack in seconds
    time_to_crack_seconds = total_combinations / guesses_per_second

    # Convert time to crack to human-readable format
    time_to_crack_minutes = time_to_crack_seconds / seconds_per_minute
    time_to_crack_hours = time_to_crack_minutes / minutes_per_hour

    return time_to_crack_hours

def get_character_set_size(complexity):
    if complexity == "low":
        return len(string.ascii_letters + string.digits)
    elif complexity == "medium":
        return len(string.ascii_letters + string.digits + string.punctuation)
    elif complexity == "high":
        return len(string.ascii_letters + string.digits + string.punctuation)

def generate_random_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_letters
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity option")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    name()

    print("Choose an option:")
    print("1. Enter a password for strength checking")
    print("2. Generate a random password")

    option = input("Enter the number corresponding to your choice: ")

    if option == "1":
        password = input("Enter a password: ")
        strength = check_password_strength(password)
        crack_time = estimate_crack_time(password, "medium")
        print(f"Strength: {strength}")
        print(f"Estimated Time to Crack: {crack_time:.2f} hours")
    elif option == "2":
        length = int(input("Enter password length: "))
        complexity = input("Enter password complexity (low/medium/high): ")
        random_password = generate_random_password(length, complexity)
        crack_time = estimate_crack_time(random_password, complexity)
        print(f"Generated Password: {random_password}")
        print(f"Estimated Time to Crack: {crack_time:.2f} hours")
    else:
        print("Invalid option. Please choose 1 or 2.")
