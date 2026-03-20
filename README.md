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
- These are some of the planning that I did before starting development.
  
  The project methodology has been structured into two distinct phases.
<img width="683" height="259" alt="image" src="https://github.com/user-attachments/assets/9b3cefed-093f-4afe-8d6c-c84909fe1af9" />









   
