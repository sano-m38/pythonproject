# Course project

# Task Description
You are tasked with building a command-line-based Task Management system using Python for a top-secret government agency. The agency deals with highly classified projects, and security is of utomost importance. Your application must provide a secure and effcient way for agents to manage their tasks  while ensuring that all data remains encrypted and protected. 

# Project tasks 
1. Implement a User class to represent a governerment agent. The user class should have attributes like agent ID, username , hased password (using a strong encryption algorithm like bcrypt), and a list of encrypted tasks associated with the agent.
2. Allow agents to register an account with a unique agent ID, username, and password. The agent ID should be provided by the agency to ensure uniquess and identification.
3. Use the cryptography library in python to implement data encryption and decryption. Use AES encryption with a strong encryption key derived from mthe user's password.
4. User should be able to:
   - Add a new task to their list, including a task description, due date, and project calssfication level (e.g., Top secrete, Secret, Confidential).
   - View all tasks in their list with the sensititve data redacted (e.g., task description and project calssification).
   - Decrypt and view sensitive task details (description) only after successful authentification with a secure token (a one-time code provided by the agency).
5. Store user account information and encrypted tasks in separate files securely.

# How did I do it ?
1. These are some of the planning that I did before starting development.
  
- The project methodology has been structured into two distinct phases.
<img width="683" height="259" alt="image" src="https://github.com/user-attachments/assets/9b3cefed-093f-4afe-8d6c-c84909fe1af9" />


- The system is composed of two main classes—User and Task—and both are designed with equal complexity, each containing three attributes and three methods.
<img width="536" height="319" alt="Screenshot 2026-03-20 145936" src="https://github.com/user-attachments/assets/15f90902-0c3b-42ed-a30c-bdadafa805b5" />

- The diagram organizes system functionality into 7 methods across two classes, clearly distinguishing between operations that:

Act on the class itself (class methods), Operate on individual objects (instance methods) and Perform utility tasks without relying on object state (static methods).
<img width="653" height="717" alt="Screenshot 2026-03-20 150228" src="https://github.com/user-attachments/assets/154f7f6f-c1b6-4ec4-8a81-fa0363f570fc" />



2. I also designed the following flow chart to understand the program flow.
<img width="890" height="643" alt="image" src="https://github.com/user-attachments/assets/afdcce14-418f-48e3-9250-e7a1327df18d" />
<img width="887" height="681" alt="image" src="https://github.com/user-attachments/assets/cf4745bf-d5cb-4526-9894-d7fbb0b5f36e" />



3. First create files:
   - 1 python file that consist the main program, second create a data json file which store agent account data and last create task json file which stores encrypted task data.
  
4. Registration process
   - When an agent registers, the system automatically generates a unique ID like AGENT6.
   The password is hashed using the bcrypt library, which means it’s converted into an irreversible hash before being stored.
   This ensures that even if someone opens the JSON file, they can’t see the real password.

   - This hash is unique every time, even for the same password, because bcrypt uses random salt.”
   As you can see when we enter the password no characters appear on the screen as a security measure. This was done using getpass which is applied in the registration and login processes. 

5. Login process 
   - During login, the entered password is verified against the stored bcrypt hash using bcrypt.checkpw()refer line 66
   If it matches, login succeeds and the agent’s information is loaded into memory.

6. Add task process
   - Each task is linked to the agent who created it via their agentID. See task.json file refer to line 13.
   The 2 variables that are encrypted are task description and project level. Before encryption, the AES key is derived from the agent’s password using an algorithm (PBKDF2). See task.json refer to line 4 and 9.
   The actual task text and project level is not visible — it’s stored as ciphertext along with a unique nonce. Only the agent who created the task can decrypt it.

7. View task process
   - If a wrong OTP is entered, the system hides the confidential data and only shows a redacted summary.
   the correct OTP (123456):
   When the correct OTP is entered, the program decrypts the data using AES CTR mode and displays the full information.

8. Logout & Exit process
   - Choose 3. LOGOUT, then 3. EXIT
   The agent logs out, and the system ends safely.


# Resources that I used 
