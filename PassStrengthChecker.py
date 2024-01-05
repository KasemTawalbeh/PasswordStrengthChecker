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
    # Existing function code...

def estimate_crack_time(password, complexity):
    # Existing function code...

def get_character_set_size(complexity):
    # Existing function code...

def generate_random_password(length, complexity):
    # Existing function code...

if __name__ == "__main__":
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
