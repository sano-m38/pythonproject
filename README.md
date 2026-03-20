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

The system is composed of two main classes—User and Task—and both are designed with equal complexity, each containing three attributes and three methods.
<img width="536" height="319" alt="Screenshot 2026-03-20 145936" src="https://github.com/user-attachments/assets/15f90902-0c3b-42ed-a30c-bdadafa805b5" />

The diagram organizes system functionality into 7 methods across two classes, clearly distinguishing between operations that:

Act on the class itself (class methods),

Operate on individual objects (instance methods), and

Perform utility tasks without relying on object state (static methods).
<img width="593" height="573" alt="Screenshot 2026-03-20 150213" src="https://github.com/user-attachments/assets/b9d7aa91-14a9-4a5d-ab7b-f65ff32c1e88" />


- I also designed the following flow chart to understand the program flow.
<img width="403" height="677" alt="image" src="https://github.com/user-attachments/assets/4ebedc1f-4e5e-45c9-aaee-7abb3c2df637" />





   
