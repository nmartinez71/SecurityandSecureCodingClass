username1 = "manager27"
username2 = "employee72"

roles = {
    username1: "admin",
    username2: "user"
}


username = input("Enter your username: ")

while username not in roles:  
    username = input("User not found. Re-enter a valid username: ")
        
role = roles[username] #assigns user role to variable from the dictionary 
print("User is", username)
print("Role is", roles[username])
    
while True:
    print("\nChoose an action:")
    print("1. Open schedule (admin only)")
    print("2. Check user data (user only)")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        if role == "admin":
            print("opening schedule...")
        else:
            print("Error: Users cannot view schedule.")

    elif choice == "2":
        if role == "user":
            print("showing employee data...")
        else:
            print("Error: Admins cannot check personal data.")

    else:
        print("\nThe choice:"+choice+" is invalid. Eneter 1 or 2")