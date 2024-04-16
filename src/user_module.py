import os
import datetime
from shared_functions import list_entries, read_credentials, write_credentials

# Define the path to the journal entries directory, relative to the current file's location.
JOURNAL_PATH = os.path.join(os.path.dirname(__file__), '..', 'journal_entries')


# Function to allow a user to write a new journal entry.
def write_entry(username):
    # Capture the current date to create a uniquely dated entry file.
    today = datetime.date.today()
    filename = f"{JOURNAL_PATH}/{username}/{today.strftime('%m-%d-%Y')}.txt"

    # Prompt the user for entry details: title, mood, and content.
    title = input("Enter title for your journal entry: ").strip()
    mood = input("How are you feeling today? ").strip()
    content = input("Write your journal entry: ").strip()

    # Ensure the user's journal directory exists; if not, create it.
    if not os.path.exists(f"{JOURNAL_PATH}/{username}"):
        os.makedirs(f"{JOURNAL_PATH}/{username}")

    # Write the user's entry to the file, appending if the file already exists.
    with open(filename, "a") as file:
        file.write(f"Title: {title}\nMood: {mood}\nContent: {content}\n\n")
    print("Journal entry saved.")


# Function to read and display a journal entry from a specific date.
def read_entry(username):
    date_input = input("Enter date (MM/DD/YYYY) to read entries: ")
    try:
        # Parse the user-provided date and format it to match the file naming convention.
        date = datetime.datetime.strptime(date_input, '%m/%d/%Y').date()
        filename = f"{JOURNAL_PATH}/{username}/{date.strftime('%m-%d-%Y')}.txt"

        # If an entry for the given date exists, read and print its contents.
        if os.path.exists(filename):
            with open(filename, "r") as file:
                print(file.read())
        else:
            print("No entries found for this date.")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YYYY.")


# Function to delete a specific journal entry for a user.
def delete_user_entry(username):
    # Check if the journal directory for the user exists.
    journal_dir = f"{JOURNAL_PATH}/{username}"
    if not os.path.exists(journal_dir):
        print("No journal entries found.")
        return

    # List existing entries and prompt the user for the date of the entry to delete.
    list_entries(username)
    entry_date = input("Enter the date of the entry you want to delete (MM-DD-YYYY): ")
    entry_file = f"{journal_dir}/{entry_date}.txt"

    # If the specified entry exists, delete it.
    if os.path.exists(entry_file):
        os.remove(entry_file)
        print(f"Entry for {entry_date} deleted.")
    else:
        print("Entry not found for the specified date.")


# Function to compute and display statistics about the user's journal entries, particularly the mood.
def view_mood_statistics(username):
    print("\nMood Statistics:")
    mood_count = {}

    # Access the user's journal directory and process each entry file.
    user_path = os.path.join(JOURNAL_PATH, username)
    if os.path.isdir(user_path):
        for filename in os.listdir(user_path):
            file_path = os.path.join(user_path, filename)
            with open(file_path, "r") as file:
                entries = file.read().split('\n\n')  # Split the content by entries.
                for entry in entries:
                    # Extract the mood line and update the count for each mood.
                    lines = entry.split('\n')
                    mood_line = next((line for line in lines if line.startswith("Mood:")), None)
                    if mood_line:
                        mood = mood_line.split("Mood: ")[1]
                        mood_count[mood] = mood_count.get(mood, 0) + 1

    # Print the count of each mood found in the entries.
    for mood, count in mood_count.items():
        print(f"{mood}: {count} time(s)")


# Function to search for journal entries that contain a specific keyword.
def search_entries(username, keyword):
    found = False
    user_path = os.path.join(JOURNAL_PATH, username)
    print("\nSearch Results:")

    # Go through each entry file in the user's journal directory.
    if os.path.isdir(user_path):
        for filename in os.listdir(user_path):
            file_path = os.path.join(user_path, filename)
            with open(file_path, "r") as file:
                entries = file.read().split('\n\n')  # Split the content by entries.
                for entry in entries:
                    # Check if the entry contains the keyword and print the title and date if it does.
                    if keyword.lower() in entry.lower():
                        title_line = next((line for line in entry.split('\n') if line.startswith("Title:")),
                                          "Title: Unknown")
                        title = title_line.split("Title: ")[1]
                        date = filename.replace('.txt', '')
                        print(f"Entry: {title} (Date: {date})")
                        found = True

    # If no entries containing the keyword were found, notify the user.
    if not found:
        print("No entries found with that keyword.")

def set_recovery_start_date(username, start_date):
    credentials = read_credentials()
    if username in credentials:
        credentials[username]["recovery_start_date"] = start_date
        write_credentials(credentials)
        print("Recovery start date set successfully.")
    else:
        print("User not found.")

def calculate_sobriety_length(username):
    credentials = read_credentials()
    if username in credentials and "recovery_start_date" in credentials[username]:
        start_date = datetime.datetime.strptime(credentials[username]["recovery_start_date"], '%Y-%m-%d').date()
        sobriety_length = (datetime.date.today() - start_date).days
        print(f"{sobriety_length} days sober.")
    else:
        print("Recovery start date not set.")

def add_milestone(username, milestone):
    credentials = read_credentials()
    if username in credentials:
        if "milestones" not in credentials[username]:
            credentials[username]["milestones"] = []
        credentials[username]["milestones"].append(milestone)
        write_credentials(credentials)
        print("Milestone added successfully.")
    else:
        print("User not found.")

def log_health_metrics(username):
    mood = input("Today's mood (1-10): ")
    cravings = input("Cravings intensity today (1-10): ")
    # Load existing data
    credentials = read_credentials()
    user_data = credentials.get(username, {})
    # Append new health metrics
    if "health_metrics" not in user_data:
        user_data["health_metrics"] = []
    user_data["health_metrics"].append({"date": str(datetime.date.today()), "mood": mood, "cravings": cravings})
    # Save updated data
    credentials[username] = user_data
    write_credentials(credentials)
    print("Health metrics logged.")


def get_recovery_tips(username):
    credentials = read_credentials()
    user_data = credentials.get(username, {})
    
    # Fetch the latest health metrics
    health_metrics = user_data.get("health_metrics", [])
    if health_metrics:
        latest_metrics = health_metrics[-1]
        mood, cravings = latest_metrics.get("mood"), latest_metrics.get("cravings")
        
        # Provide tips based on the latest mood and cravings
        if int(cravings) > 7:
            print("High cravings detected. Consider engaging in a distracting activity, like a hobby or exercise.")
        elif int(mood) < 4:
            print("It seems you're having a tough day. Remember, it's okay to ask for help. Reach out to a friend or a support group.")
        else:
            print("You're doing great! Keep up the good work.")
    else:
        print("No health metrics found. Consider logging your mood and cravings to get personalized recovery tips.")


def access_motivational_resources(username):
    credentials = read_credentials()
    user_data = credentials.get(username, {})
    
    # Check the number of milestones to gauge the recovery stage
    milestones = user_data.get("milestones", [])
    if len(milestones) < 3:
        print("Early in your recovery journey? Watch 'The Road to Recovery' on YouTube for inspiration.")
    else:
        print("Looking for motivation? Read 'Staying Sober: Tips for Working a Twelve Step Program of Recovery'.")


def add_milestone(username, milestone):
    # Extracting milestone details
    milestone_type, date, description = milestone.split(":", 2)
    
    credentials = read_credentials()
    user_data = credentials.get(username, {})
    
    if "milestones" not in user_data:
        user_data["milestones"] = []
    
    user_data["milestones"].append({"type": milestone_type, "date": date, "description": description})
    
    # Save updated data
    credentials[username] = user_data
    write_credentials(credentials)
    print(f"Milestone added for {username}: {description} on {date}")

def display_user_details(username):
    # Load the user credentials and details
    credentials = read_credentials()
    user_data = credentials.get(username, {})

    # Fetch recovery start date
    recovery_start_date = user_data.get("recovery_start_date", "Not set")
    print(f"Recovery Start Date: {recovery_start_date}")

    # Fetch and display milestones
    milestones = user_data.get("milestones", [])
    if milestones:
        print("\nMilestones:")
        for milestone in milestones:
            print(f" - {milestone}")
    else:
        print("\nMilestones: None")

    # Fetch and display health metrics
    health_metrics = user_data.get("health_metrics", [])
    if health_metrics:
        print("\nHealth Metrics:")
        for metric in health_metrics:
            date = metric.get("date", "Unknown date")
            mood = metric.get("mood", "N/A")
            cravings = metric.get("cravings", "N/A")
            print(f" - Date: {date}, Mood: {mood}, Cravings: {cravings}")
    else:
        print("\nHealth Metrics: None")


# Function to allow a user to delete their own account.
def delete_own_account(username):
    print(f"Deleting account for {username}...")
    credentials = read_credentials()

    # Check if the user exists in the credentials and delete if present.
    if username in credentials:
        del credentials[username]
        write_credentials(credentials)
        print("Your account has been successfully deleted.")
        return True  # Indicates account deletion was successful
    else:
        print("Account not found.")
        return False
