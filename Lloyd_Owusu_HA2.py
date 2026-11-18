
# Template provided lists
upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

database = [
    "Jake:A-B-a-b-c-C",
    "Mary:B-z-z-r-R-b",
    "Bob:X-y-a-Z-i-d",
    "Janet:c-d-N-m-h-H",
    "Henry:G-i-K-o-o-e"
]

def validate_password(password):
    """
    Helper function to validate password criteria:
    - 2 uppercase letters
    - 4 lowercase letters
    - Separated by '-'
    - No digits or other special characters
    Returns (is_valid, upper_count, lower_count)
    """
    upper_count = 0
    lower_count = 0
    
    # Split password by '-' delimiter to check individual characters
    parts = password.split('-')
    
    # Password must have exactly 6 characters separated by hyphens (5 hyphens)
    if len(parts) == 6:
        for part in parts:
            if part in upper_case_letters:
                upper_count += 1
            elif part in lower_case_letters:
                lower_count += 1
                
    # Check overall string counts
    is_valid = (upper_count == 2) and (lower_count == 4) and (len(password) == 11)
    return is_valid, upper_count, lower_count


# Main Program Loop
while True:
    print("******** Welcome to Password storage and Management system *********")
    print("Available options:")
    print("1: Display usernames and passwords")
    print("2: Add password")
    print("3: Update password by username")
    print("4: Exit")
    
    choice = input("Enter option: ").strip()

    # OPTION 1: Display usernames and passwords
    if choice == "1":
        print("******** Displaying list of passwords and usernames ********")
        for record in database:
            # Split username and password explicitly by delimiter ':'
            username, password = record.split(":")
            print("Username {}: Password {}".format(username, password))

    # OPTION 2: Add username and password
    elif choice == "2":
        print("******** Add username and password to the database********")
        username = input("Enter your username: ").strip()
        
        # Check if username already exists in database
        existing_users = [rec.split(":")[0] for rec in database]
        if username in existing_users:
            print("Username already exists in the database. Please try a different username.")
            continue

        password = input("Enter your password (Example: h-i-P-h-O-p): ").strip()
        
        # Validate password using loop logic
        is_valid, upper_cnt, lower_cnt = validate_password(password)
        
        if is_valid:
            print("Password Accepted!")
            print(password)
            entry = "{}:{}".format(username, password)
            database.append(entry)
            print("Adding username and password {} to the database".format(entry))
        else:
            print("Password Rejected")
            print("Number of uppercase letters {} and Number of lower case letters {}".format(upper_cnt, lower_cnt))

    # OPTION 3: Update password for existing user
    elif choice == "3":
        print("******** Update password of an existing user ********")
        target_user = input("Enter the username you would like to update the password: ").strip()
        
        found_index = -1
        for i in range(len(database)):
            user, pwd = database[i].split(":")
            if user == target_user:
                found_index = i
                break
                
        if found_index != -1:
            new_password = input("Enter the new password: ").strip()
            is_valid, upper_cnt, lower_cnt = validate_password(new_password)
            
            if is_valid:
                database[found_index] = "{}:{}".format(target_user, new_password)
                print("Password updated for user: {}".format(target_user))
                print(new_password)
            else:
                print("Password Rejected")
                print("Number of uppercase letters {} and Number of lower case letters {}".format(upper_cnt, lower_cnt))
        else:
            print("User not found in the database.")

    # OPTION 4: Exit program
    elif choice == "4":
        break

    # Invalid choice handling
    else:
        print("Not a valid selection. Please try again.")
