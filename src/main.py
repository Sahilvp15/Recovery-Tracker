# main.py
# This is the entry point of the Journal App where user interaction is handled.

# Import necessary functions from other modules
from admin_module import (
    create_admin_account, admin_create_user, admin_view_user_journal,
    delete_user, admin_view_user_info
)
from user_module import (
    write_entry, read_entry, delete_user_entry, view_mood_statistics,
    search_entries, delete_own_account
)
from shared_functions import (
    list_entries, read_credentials, write_credentials, login, register_user
)

from user_module import (
    set_recovery_start_date, add_milestone, calculate_sobriety_length,
)

from user_module import (
    log_health_metrics, get_recovery_tips, access_motivational_resources, display_user_details
)

# Function to print a menu with given options and a title
def print_menu(options, title="Menu"):
    # Print the menu header
    print("\n" + "=" * 30)
    print(f"{title}".center(30))
    print("=" * 30)
    # Print each menu option
    for key, value in options.items():
        print(f"{key}. {value}")

def main():
    # Ensures the admin account is created at startup
    create_admin_account()

    while True:
        # Welcome message and role selection
        print("\n" + "-" * 50)
        print("WELCOME TO RECOVERY TRACKER".center(50))
        print("-" * 50)
        user_type = input("Select your role:\n1. Admin \n2. New User \n3. Returning User \n4. Log Out \nYour choice [1/2/3/4]: ").strip().lower()

        # Admin role functionalities
        if user_type == '1':
            # Attempt to log in as admin
            username = login()
            if username == 'admin':
                print(f"\nWelcome, Admin {username}!")
                while True:
                    # Admin action options
                    admin_options = {
                        "1": "Create a User",
                        "2": "View User Info",
                        "3": "Delete a User",
                        "4": "View User Journals",
                        "5": "Log Out"
                    }
                    # Display the admin menu
                    print_menu(admin_options, "Admin Actions")
                    admin_choice = input("Enter choice: ")

                    # Execute the selected admin option
                    if admin_choice == '1':
                        admin_create_user()
                    elif admin_choice == '2':
                        admin_view_user_info()
                    elif admin_choice == '3':
                        delete_user(username)
                    elif admin_choice == '4':
                        admin_view_user_journal(username)
                    elif admin_choice == '5':
                        break  # Logging out
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Admin login failed.")

        # New or Returning User functionalities
        elif user_type in ['2', '3']:
            # Register a new user
            if user_type == '2':
                register_user()
                continue

            # Attempt to log in as user
            username = login()
            if username:
                print(f"\nWelcome, {username}!")
                while True:
                    # User action options
                    user_options = {
                        "1": "Write new entry",
                        "2": "Read an entry",
                        "3": "View mood statistics",
                        "4": "Search entries",
                        "5": "List all entries",
                        "6": "Delete an entry",
                        "7": "Delete your account",
                        "8": "Set Recovery Start Date",  
                        "9": "Add Milestone", 
                        "10": "View Sobriety Length",  
                        "11": "Log Health Metrics",  
                        "12": "Get Recovery Tips",  
                        "13": "Access Motivational Resources",
                        "14": "Display Recovery Progress",
                        "15": "Log Out"
                    }
                    # Display the user menu
                    print_menu(user_options, "RECOVERY TRACKER")
                    choice = input("Enter choice: ")

                    # Execute the selected user option
                    if choice == '1':
                        write_entry(username)
                    elif choice == '2':
                        read_entry(username)
                    elif choice == '3':
                        view_mood_statistics(username)
                    elif choice == '4':
                        keyword = input("Enter keyword to search: ")
                        search_entries(username, keyword)
                    elif choice == '5':
                        list_entries(username)
                    elif choice == '6':
                        delete_user_entry(username)
                    elif choice == '7':
                        # Attempt to delete the user's own account
                        if delete_own_account(username):
                            break  # Exit if account deletion is successful
                    elif choice == '8':
                        start_date = input("Enter your recovery start date (YYYY-MM-DD): ")
                        set_recovery_start_date(username, start_date)
                    elif choice == '9':
                        milestone_description = input("Enter milestone description (e.g., '30 days sober'): ")
                        milestone_date = input("Enter the date for this milestone (YYYY-MM-DD): ")
                        add_milestone(username, f"{milestone_date}: {milestone_description}")
                    elif choice == '10':
                        calculate_sobriety_length(username)
                    elif choice == '11':
                        log_health_metrics(username)
                    elif choice == '12':
                        get_recovery_tips(username)
                    elif choice == '13':
                        access_motivational_resources(username)
                    elif choice == '14':
                        display_user_details(username)
                    elif choice == '15':
                        break  # Logging out
                    else:
                        print("Invalid choice. Please try again.")

        # Exit the application
        elif user_type == '4':
            print("\nLogging out of the program. Goodbye!")
            break
        
        else:
            print("Invalid selection. Please enter '1', '2', '3', or '4'.")

# Check if the script is the main program and run it
if __name__ == "__main__":
    main()
