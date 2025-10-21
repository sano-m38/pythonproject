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

# Optional tasks 
1. Use argparse module to handle command-line arguments and create a user-friendly command-line interface.
An example is shown below:
<img width="234" height="192" alt="image" src="https://github.com/user-attachments/assets/75025ffb-c625-486a-bf64-2e9e345cec0f" />
<br>
2. Design a mechanism to handle password resets with strong security checks to ensure the agent's identity.
3. create a separate log file that records all user activities (e.g login attempts, task updates) for auditing purposes, ensuring that this log file is also encrypted and accessible only to authorised personnel (implement authorisation_level attribute in the User class).
<br>
<br>
After developing the tool, you should upload it to github in a new repository.


Report 
You should also write a very brief report (1-2 pages) describing the tool that you developed. include the challenges and difficulties that you faced during the development of the software and how you managed to overcome them. You should also describe the functionality that you managed to implement and what you were not able to. 



















   
