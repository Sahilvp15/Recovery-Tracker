# Recovery Tracker
 
## Project Objectives

Our project aims to develop a comprehensive software application that supports individuals in understanding, managing, and overcoming drug abuse and addiction. We have created an application that combines robust data handling with a user-friendly interface to help the rehabilitation process.

**Key Objectives:**

- **Personal Recovery Monitoring:** Our application allows users to effectively monitor their personal recovery journey. Through our **main.py** script, users can log and review recovery milestones and daily experiences, including any challenges they face. This script is crucial for enabling users to add, view, and manage their recovery milestones and journal entries, offering an insightful overview of their progress.

- **Health Metrics Visualization:** We are committed to providing actionable insights into users' health by tracking mood and cravings. Managed by our **user_module.py**, the application allows users to input and visualize these health metrics. This functionality not only helps users track their daily well-being but also equips healthcare providers with data to make informed treatment decisions.

- **Secure and Private User Management:** Our **admin_module.py** is designed to ensure robust security and privacy protections. It handles user registration and authentication, maintaining the confidentiality of personal data. This module is essential to fostering a secure environment where users feel comfortable sharing sensitive information.

- **Accessibility and Ease of Use:** The application is engineered to be accessible to all users, regardless of their tech-savviness. The **main.py** script provides a straightforward navigation system and clear instructions, making it easy for anyone to use the application without feeling overwhelmed.

- **Support and Resources:** While primarily focused on tracking and data visualization, the application also includes motivational tips and recovery advice through user_module.py. These resources aim to educate users about addiction and support their recovery efforts, offering a well-rounded approach to rehabilitation.

By focusing on these objectives, our project seeks to provide a structured tool that not only tracks recovery but also enhances the user's ability to understand and manage their addiction patterns effectively.

## Significance Of The Project

Our project, centered around developing a comprehensive software application for managing drug abuse and addiction recovery, stands out for its meaningful contribution to public health and personal well-being. Unlike traditional treatment tracking tools, our application introduces an innovative blend of personal journaling, milestone tracking, and health metrics visualization. This triad of features not only assists individuals in monitoring their recovery but also provides healthcare providers with actionable insights into their patients' progress.

The novelty of our application lies in its user-centric design, which emphasizes privacy, user-friendliness, and comprehensive support. By integrating these elements, we offer a personalized recovery experience that is adaptable to the unique needs of each user. Our application goes beyond mere data tracking; it empowers users to gain a deeper understanding of their behavioral patterns and the effectiveness of their treatment plans. This insight is crucial for making informed adjustments that enhance recovery outcomes. Also, our project leverages advanced data structures and algorithms to ensure that the application is not only functional but also intuitive and responsive. This technological approach allows for real-time updates and feedback, which are essential for users who require consistent support and motivation. The inclusion of educational resources and direct links to professional help within the application further enriches the user's journey towards recovery.

The significance of our project extends to its potential impact on families and communities. By providing a tool that supports recovery and promotes understanding, we foster a more compassionate environment where individuals struggling with addiction are met with support rather than stigma. This shift in dynamics can significantly amplify the overall health and harmony within communities, making our application a valuable asset in the ongoing battle against drug abuse and addiction.

## Installation And Instruction To Use

### Installation
**For Windows and macOS:**
1. Ensure Python 3.8 or higher is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Our application is designed to operate using Python's standard library, it is not necessary to install any external libraries, simplifying setup and maintenance.
   
4. Clone the repository:
   ```bash
   git clone git@github.com:Sahilvp15/Recovery-Tracker.git
   cd Recovery-Tracker
   ```
  
### Instructions to Use
1. Start the application by running the main script. Make sure you are still in the project's root directory:
   ```bash
   python main.py
   ```
  This command will start the application in the command line interface.

2. Using the application:
- **Register or Log In**: Follow the prompts to register as a new user or log in with existing credentials.
- **Navigate through the application:** Use the command line options to access different features such as adding milestones, updating personal information, or adding journal entries.
- **Journal and Milestones:** Enter your daily experiences and track significant achievements as part of your recovery process.
- **Health Metrics**: Regularly update and review health metrics as prompted by the application.

## Structure of the Code

Our application is structured around four main Python modules, each serving distinct roles within the system:

1. **admin_module.py**
- Purpose: Handles administrative functions related to user management.
**Functions:**
- admin_exists(): Checks if the admin account already exists in the credentials.
- create_admin_account(): Creates an admin account if it doesn't exist.
- admin_create_user(): Allows the admin to create a new user account.
- admin_view_user_info(): Allows the admin to view user information.
- admin_view_user_journal(): Allows the admin to view user journals.
- delete_user(): Allows the admin to delete a user account.
2. **shared_functions.py**
- Purpose: Provides utility functions that are used across the application.
**Functions**:
- hash_password(): Hashes a password using SHA-256 for secure storage.
- read_credentials(): Reads the user credentials from a JSON file.
- write_credentials(): Writes updated credentials back to the JSON file.
- login(): Handles user login by checking entered credentials against stored ones.
- register_user(): Registers a new user, ensuring unique username and email.
- display_users(): Displays a list of all registered users.
- list_entries(): Lists all journal entries for a specific user.
3. **main.py**
- Purpose: Acts as the entry point for the application, orchestrating user interactions and managing the application flow.
**Main Functionality:**
- Initiates the user interface.
- Calls functions from other modules based on user input.
- print_menu(): Prints a menu with the given options and a title.
4. **user_module.py**
- Purpose: Manages functionalities specific to the user's personal data and recovery tracking.
**Functions:**
- write_entry(): Allows a user to write a new journal entry.
- read_entry(): Allows a user to read a journal entry from a specific date.
- delete_user_entry(): Allows a user to delete a specific journal entry.
- view_mood_statistics(): Computes and displays statistics about the user's journal entries, particularly the mood.
- search_entries(): Allows a user to search for journal entries that contain a specific keyword.
- set_recovery_start_date(): Allows a user to set their recovery start date.
- calculate_sobriety_length(): Calculates the user's sobriety length based on the recovery start date.
- add_milestone(): Allows a user to add a new milestone to their recovery progress.
- log_health_metrics(): Allows a user to log their daily mood and cravings.
- get_recovery_tips(): Provides personalized recovery tips based on the user's latest health metrics.
- access_motivational_resources(): Provides access to motivational resources based on the user's recovery stage.
- display_user_details(): Displays the user's recovery start date, milestones, and health metrics.
- delete_own_account(): Allows a user to delete their own account.

![Recovery_Tracker_UML](https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/617c82a0-4d13-4211-9392-33f7e4df7619)

### Interaction Between Modules
**Data Flow:** main.py serves as the controller that uses functions from admin_module.py and user_module-3.py to handle data input and operations. All modules interact with shared_functions.py for data management and utility operations like hashing.
**User Commands:** Users interact primarily through main-8.py, which directs commands to appropriate modules based on the operation (e.g., registering a user, adding journal entries).

## Functionalities and Test Results
Our Recovery Tracker application is designed to be an interactive tool for users and administrators to monitor and manage the recovery process from drug abuse and addiction. Below is an extensive overview of the application's functionalities and the test results to verify its performance.

## 1. Admin Login
### Test Procedure:
Log in as an admin. Select "View User Info" from the admin menu.
Enter the username of the account you wish to view.

### Expected Result:
The selected user's information is displayed, including username, email, and age.

<img width="378" alt="Screenshot 2024-04-15 at 10 35 24 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/a7061cea-f774-42d1-a0ca-27e1362668b5">

### Backend Operation:
**Admin_view_user_info()** function in **admin_module.py** retrieves and displays the user's details from the stored credentials.

## 1.1 Admin Actions
After the Admin logs in, it opens a whole new door of our application. It allows users to perform several functions such as:-

### Create a new user
When Admin presses 1, it allows the admin to create a user after entering all of the new users information.

<img width="372" alt="Screenshot 2024-04-15 at 10 42 19 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/ae7c6141-d04a-4ffc-8c5a-57efcb0652d5">

### View User info
When Admin presses option 2, our application provides admin with all the users names in our system they want to see their information of. After entering a certain user, it provides full list of all of that user's information. 

<img width="408" alt="Screenshot 2024-04-15 at 10 43 46 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/42dff422-203d-4ce1-ab99-d533645502d6">

### Delete a User
When the Admin selects the option 3, it allows them to delete a certain user after entering the information of the user they want to delete. 

<img width="522" alt="Screenshot 2024-04-15 at 10 51 00 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/286a3d9c-66fd-491a-bf15-15fc661795d8">

### View User Journals
When the Admin selects the option 4, the application allows the user to see any specific diary entry from any users in our system.

<img width="926" alt="Screenshot 2024-04-15 at 10 54 34 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/856c7ea8-49b1-4435-9df1-f409b5744b68">

### Logout
After performing all the desired actions, the Admin can select option 5 to logout of the system.

<img width="232" alt="Screenshot 2024-04-15 at 10 56 34 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/f87d91c3-6186-4213-80d0-cbd8fe796e57">

## 2. New User

### Test Procedure:
Run the Recovery Tracker application. Choose "New User" to initiate the registration process. Input the required details for username, email, age, and password. Also, when you are typing the password no one can see what you are typing for secuirty reasons so type carefully.

<img width="376" alt="Screenshot 2024-04-15 at 10 10 36 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/65776c12-cb45-4f38-ac81-8ca1a0d5a727">
<img width="386" alt="Screenshot 2024-04-15 at 10 29 48 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/a80524e4-5b50-4c8e-9b06-37d17ce44fe6">
<img width="692" alt="Screenshot 2024-04-15 at 10 31 09 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/c8ee6e03-7fe5-4a7f-9c5d-c519d195276e">


### Expected Result:
A new user account is created with the given details.
A confirmation message is displayed upon successful registration.

### Backend Operation:
**Register_user()** function in **Shared_functions.py** is invoked, which adds the new user to the credentials after validating the input and ensuring uniqueness.

## 3. Returning Users

### 3.1 Write New Entry
Allows users to write and save a new journal entry documenting their daily experiences, feelings, and progress.

**Instrutions:**
- Run the Recovery Tracker application.
- Select "Returning User" and log in with your credentials.
- Choose "Write new entry" by entering 1 from the user menu.
- Input the title, your current mood, and the content of your journal entry when prompted.

<img width="902" alt="Screenshot 2024-04-15 at 1 46 46 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/fa333c92-96ea-4f25-8d1e-cb6e209d31a7">
<img width="335" alt="Screenshot 2024-04-15 at 1 46 57 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/2e7992ed-1946-48ae-a9c4-92814cfe7945">

**Expected Result:**
- A new journal entry is created under your username with the provided details. A confirmation message "Journal entry saved" is displayed.

**Backend Operation:**
- The **write_entry()** function in **user_module.py** is called. This function prompts for entry details and appends the information to a text file representing the user's journal for the current date.

### 3.2 Read an entry
It allows users to retrieve and read journal entries from a specific date.

**Instructions:**
- After logging in, select "Read an entry" by entering 2 from the user menu.
- Enter the date of the journal entry you wish to read in the specified format.

![image](https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/0e7bf633-2085-42bb-aa8c-e910def30391)

**Expected Result:**
- The content of the journal entry for the given date is displayed. If no entry exists for that date, a message stating "No entries found for this date" is shown.

**Backend Operation:**
- The **read_entry()** function searches the user's journal directory for an entry file matching the date provided and displays its contents if found.

### 3.3 View Mood Statistics

**Instructions:**
- From the main menu, select "View mood statistics" by entering 3 after logging in.
- The application will process and display statistics without any additional input.
  
<img width="492" alt="Screenshot 2024-04-15 at 4 33 33 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/34ce43d5-b53d-4cc8-9725-a8a891b2ab97">

**Expected Result:**
A summary of mood occurrences in your journal entries is displayed, such as "Happy: 5 time(s)".

**Backend Operation:**
**View_mood_statistics()** in **user_module.py** analyzes the mood information from all journal entries and provides a count of each mood type.

### 3.4 Search entries

**Instructions:**
Select "Search entries" by entering 4 and when prompted, input a keyword you would like to search for in your journal entries.

<img width="255" alt="Screenshot 2024-04-15 at 4 36 21 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/a2893b2f-9cce-4ef0-af8d-9a4aeedf3a57">
<img width="1042" alt="Screenshot 2024-04-15 at 4 36 48 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/f2e2acae-c720-4121-b02b-0837cb0f6c41">

**Expected Result:**
Entries containing the keyword are listed with their titles and dates.
If no entries contain the keyword, "No entries found with that keyword" is displayed.
**Backend Operation:**
**Search_entries()** looks through the user's journal entries for the keyword and displays each matching entry.

### 3.5 List all entries

**Instructions:**
Choose "List all entries" from the menu by entering 5. No additional input is needed.

<img width="393" alt="Screenshot 2024-04-15 at 4 42 24 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/e92f81a3-29e1-47c8-afc1-c8dd17f8a817">

**Expected Result:**
All journal entries for the user are listed by date and title.
**Backend Operation:**
**List_entries()** in **shared_functions.py** compiles a list of all journal entry filenames for the user, presenting them in an organized manner.

### 3.6 Delete an entry

**Instrutions:**
Log in and select "Delete an entry" by typing 6. You'll be prompted to enter the date of the entry you want to delete.

<img width="517" alt="Screenshot 2024-04-15 at 4 50 11 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/fde80a79-1bd5-4307-91af-175a90fb15f0">

**Expected Result:**
The specified entry is deleted, and "Entry for the specific date you entered is deleted" confirms the action.
**Backend Operation:**
**Delete_user_entry()** in **user_module.py** removes the specified file from the user's journal directory.

### 3.7 Delete your account

**Instructions:**
Inside the user menu, choose "Delete your account" and confirm your decision when prompted.
<img width="692" alt="Screenshot 2024-04-15 at 10 31 09 AM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/c8ee6e03-7fe5-4a7f-9c5d-c519d195276e">
<img width="372" alt="Screenshot 2024-04-15 at 5 00 38 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/cb6a40eb-4b30-4758-b36a-3b5d892761a1">
<img width="722" alt="Screenshot 2024-04-15 at 5 01 48 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/997e2c7c-a022-4438-8f37-2d6efc6e6ac9">

**Expected Result:**
The user's account and all associated data are permanently removed, with a message confirming the deletion.
**Backend Operation:**
**Delete_own_account()** from **user_module.py** erases the user's credentials and journal entries from the system.

### 3.8 Set Recovery Start Date

**Instruction:**
From the user options, select "Set Recovery Start Date" and input the date when prompted.

<img width="408" alt="Screenshot 2024-04-15 at 5 08 06 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/a744b76b-9cbd-470e-bf9b-5950665e983a">
<img width="640" alt="Screenshot 2024-04-15 at 5 08 23 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/24be1928-cae0-45a7-833f-028ad1528e74">

**Expected Result:**
The user's recovery start date is updated in the system, with a confirmation message.
**Backend Operation:**
**Set_recovery_start_date()** updates the user's credentials with the specified start date for recovery tracking.

### 3.9 Add Milestone
**Instruction:**
Choose "Add Milestone" from the menu by entering 9, then input the description and date for the milestone.

<img width="1077" alt="Screenshot 2024-04-15 at 5 22 20 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/a5d08a67-15ea-4a74-afde-6e53cb648bbb">
<img width="915" alt="Screenshot 2024-04-15 at 5 22 33 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/93911302-7ddc-4a95-8762-4529bc85715d">

**Expected Result:**
The milestone is added to the user's account, confirmed by a success message.
**Backend Operation:**
**Add_milestone()** records the milestone in the user's credentials file under their account information.

### 3.10 View Sobriety Length
**Test Procedure:**
Log in and select "View Sobriety Length" to automatically calculate and display the duration of sobriety based on the start date.

<img width="243" alt="Screenshot 2024-04-15 at 5 28 30 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/5d1c2943-b4a5-43f6-8ee1-95b41b4a803a">

**Expected Result:**
The length of sobriety in days is displayed to the user.
**Backend Operation:**
**Calculate_sobriety_length()** computes the difference between the current date and the recovery start date.

### 3.11 Log Health Metrics
**Test Procedure:**
Select "Log Health Metrics" by entering 11 and input your current mood and craving levels when prompted. These log metrics are used for other features in our program.

<img width="260" alt="Screenshot 2024-04-15 at 5 31 40 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/c08a185b-1899-4093-8c9e-2e1dec246519">
<img width="874" alt="Screenshot 2024-04-15 at 5 32 05 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/f324183e-d135-4e7a-acce-4a3bdba6b00d">

**Expected Result:**
Today's health metrics are logged into your account, with a message confirming the log.
**Backend Operation:**
**Log_health_metrics()** captures and stores the user's self-reported health data in their credentials file.

### 3.12 Get Recovery Tips
**Instruction:**
Choose "Get Recovery Tips" from the menu by entering 12, and the system will automatically provide personalized tips by using your log metrics of the day. It gives personalized tips according to your log metrics. These are two examples below:-

<img width="308" alt="Screenshot 2024-04-15 at 5 38 21 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/79642a7c-db71-4446-b6c6-f291b91931dd">
<img width="673" alt="Screenshot 2024-04-15 at 5 38 29 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/febc2661-9df0-4b68-a3e7-620c1b763d97">


**Expected Result:**
Tips and suggestions for recovery are displayed based on the latest health metrics.
**Backend Operation:**
**get_recovery_tips()** analyzes the most recent health metrics and offers tailored advice to the user.

### 3.13 Access Motivational Resources
**Instruction:**
Users can opt for "Access Motivational Resources" from the menu to get motivational content recommendations by entering 13 which will give reccomendations based on recovery period.

<img width="643" alt="Screenshot 2024-04-15 at 5 41 32 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/ab0c4f8c-f90a-4361-9d90-183962713705">

**Expected Result:**
Suggestions for motivational resources, such as articles or videos, are presented to the user.
**Backend Operation:**
**access_motivational_resources()** assesses the user's progress and suggests resources accordingly.

### 3.14 Display Recovery Progress
**Instructions**
From the menu, users can select "Display Recovery Progress" to view a comprehensive report of their recovery journey.
<img width="1071" alt="Screenshot 2024-04-15 at 5 44 08 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/f452f568-acb0-4bb8-9a80-cabf3cdbff9d">

**Expected Result:**
A detailed view of the user's milestones, sobriety length, and health metrics is shown.
**Backend Operation:**
**display_user_details()** compiles and displays data from various parts of the user's account to provide an overview of their recovery progress.

### 3.15 Logout

**Instruction:**
Select "Log Out" to end your session with the application.

<img width="379" alt="Screenshot 2024-04-15 at 5 49 53 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/acb836f0-8fab-46e5-b251-49891eceb55a">

**Expected Result:**
The user is logged out, and the application returns to the main role selection menu.
**Backend Operation:**
This action terminates the user's session and clears any temporary data related to the session.

## 4 Log out
**Instruction:**
After the user is logged out, they can select "Log Out" by pressing 4 to logout of the whole application to end their session.

<img width="370" alt="Screenshot 2024-04-15 at 5 51 01 PM" src="https://github.com/Kunj-13/Recovery-Tracker/assets/143433713/d68ba24b-f586-41a8-b203-6eb729b4b0a6">

**Expected Result:**
The application is terminated and a message is displayed of "Logging out of the program. Goodbye!".

## Discussion & Conclusion
Throughout the development of our Recovery Tracker application, we faced several challenges and limitations, each providing a valuable learning opportunity aligned with our course topics.

- One significant issue was ensuring robust data security and privacy. Initially, our application relied on basic password hashing, which presented risks regarding the integrity and confidentiality of user data. To address this, we have begun exploring more advanced encryption methods and access control mechanisms, inspired by our studies on Security and Protection. This course segment taught us the importance of comprehensive security measures, which we implemented to enhance user trust and data safety.

- Another limitation was the insufficient data visualization tools within our application. Our initial focus was more on data collection than on interpretation, which limited the application’s utility in providing actionable insights. Drawing on our knowledge from the File-System and I/O Systems topics, we integrated more sophisticated visualization tools and reporting features. These enhancements will enable users to see trends and gain personalized insights into their recovery process, making the data collected much more beneficial.

- **Customization and Personalization:** Initially, our application offered limited customization, which could hinder user engagement and satisfaction. The learnings from the Distributed Systems topic have been crucial here, guiding us to develop a more adaptable architecture that supports extensive personalization features. This approach allows the application to cater more effectively to individual user needs, fostering a greater sense of ownership and engagement. By putting in the effort, we have transformed the Recovery Tracker into an effective, secure, and user-friendly tool that not only supports individuals in their recovery journeys but also enhances our understanding of technological applications in real-world scenarios, demonstrating the practical impact of our academic learnings on real-life challenges. This project contributes positively to broader public health outcomes by providing a tool that supports recovery and promotes understanding, helping to reduce the stigma associated with addiction.
