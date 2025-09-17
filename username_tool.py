# Username Validator & Generator

def main():
    print("=== Social Media Username Tool ===")
    print("1. Check username")
    print("2. Generate username")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        check_username()
    elif choice == "2":
        generate_username()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice!")

def check_username():
    # TODO: Implement username checker
    pass

def generate_username():
    # TODO: Implement username generator
    pass

# Run the program
main()