# latest version functional 02.09.25 (fixed)
import json
import bcrypt
from getpass import getpass

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os


# OTP 123456

with open("data.json", "r") as file:
    data = json.load(file)


def derive_key_from_password(password: str) -> bytes:
    # Derive 32-byte key from password (AES-256)
    return PBKDF2(password, b"", dkLen=32, count=100000)



class User:
    registered_users = []
    def __init__(self, unique_agentID, name, password):
        self.unique_agentID = unique_agentID
        self.name = name
        self.password = password
        User.registered_users.append(self)  

    @classmethod
    def register(cls, name, password):
        unique_agentID = User.create_agentID()
        ux1 = User(unique_agentID, name, password)
        ux1.store_userACinfo(unique_agentID, name, password) #b1 (b=bookmark to compare testproject.py (our version) v/s tp.py(chatgpt's debugged version) in PROPY for the problem of 'pressing 3 times number 3 to exit')
        return ux1

    @classmethod
    def create_agentID(cls):
        return len(data["users"]) + 1 #b2

    def store_userACinfo(self, unique_agentID, name, password): #b3
        bd = password.encode('utf-8') #convernting string to byte
        hashed_password= bcrypt.hashpw(bd,bcrypt.gensalt()) #generating the hash: converting byte into hash
        hashed_password_str = hashed_password.decode('utf-8') #convert hash to string. string needed because json accepts only string
        data["users"].append({
            "agentID": f"AGENT{unique_agentID}", 
            "name": name, 
            "password": hashed_password_str
        })
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def login(cls): 
        print("\n--- LOGIN AGENT ---")
        name = input("ENTER NAME: ")
        password = getpass("ENTER PASSWORD: ")
        bd = password.encode('utf-8') #convernting string to byte
        hashed_password= bcrypt.hashpw(bd,bcrypt.gensalt()) #generating the hash
        # hashed_password_str = hashed_password.decode('utf-8') #convert hash to string. string needed because json accepts only string


        for user in data["users"]:
            # if user["name"] == name and user["password"] == hashed_password_str:
            if user["name"] == name and bcrypt.checkpw(bd,hashed_password):          
                print("\nLOGIN SUCCESSFUL.")
                return User(user['agentID'], user['name'], user['password']) #here we are returing a user object. so the return send the user object back to wherever we call the login method on the User class, that is the User.login
        print("\nLOGIN FAILED.") 
        return None #b4




class Task:
    task_list = []
    def __init__(self, task_description, due_date, project_level,agentID):
        self.task_description = task_description
        self.due_date = due_date
        self.project_level = project_level
        self.agentID = agentID
        Task.task_list.append(self)
        
    def add_task(self, file_path):
        with open(file_path, "r") as file:
            task = json.load(file)

        task_description = input("ENTER TASK DESCRIPTION: ")
        due_date = input("ENTER DUE DATE: ")
        project_level  = input("\nENTER PROJECT CLASSIFICATION LEVEL:\n"
                                "*TOP SECRET* | *SECRET* | *CONFIDENTIAL*\n")
        

        # --- derive key from password ---
        key = derive_key_from_password(self.password)

        # --- encrypt task description ---
        cipher1 = AES.new(key, AES.MODE_CTR)
        ct_description = cipher1.encrypt(task_description.encode('utf-8'))

        # --- encrypt project level ---
        cipher2 = AES.new(key, AES.MODE_CTR)
        ct_project = cipher2.encrypt(project_level.encode('utf-8'))



        # --- store ciphertexts + nonces instead of plaintext ---
        Task.store_task(file_path, task,
                        {"ciphertext": ct_description.hex(), "nonce": cipher1.nonce.hex()},
                        due_date,
                        {"ciphertext": ct_project.hex(), "nonce": cipher2.nonce.hex()},
                        self.agentID)

        # Task.store_task(file_path, task, task_description, due_date, project_level,self.agentID) #But why self and not Task.agentID? see below.
        print(f"\nTask '{task_description}' added successfully.\n")                             #This comes down to instance attributes vs class attributes. self.agent_ID → belongs to this particular instance of the Task class. 
                                                                                                # #Every task can have a different agent_ID.  Task.agentID → would refer to a class attribute, shared by all instances of Task. 
                                                                                                # #That would mean all tasks share the same agent_ID, which is not what you want.


















    @staticmethod
    def store_task(file_path, task, task_description, due_date, project_level,agentID):
        task["tasks"].append({
            "task description": task_description, #b5
            "due date": due_date, #b6
            "project level": project_level, #b7
            "agentID": agentID
        })
        with open(file_path, "w") as file:
            json.dump(task, file, indent=4)


    def view_task(self,file_path,agentID):
        with open(file_path, "r") as file:
            task = json.load(file)

        print("\n--- VIEW TASKS ---")
        otp = input("ENTER ONE-TIME CODE TO DECRYPT SENSITIVE DATA: ")

        if otp != "123456":   # temporary hardcoded OTP
            print("INVALID OTP. Showing redacted view only.")
            for d in task["tasks"]:
                if d["agentID"] == agentID:
                    print(f"Task description: [REDACTED] | Due date: {d['due date']} | project classification level: [REDACTED]")
            return


        # --- derive key from password ---
        key = derive_key_from_password(self.password)


        for d in task["tasks"]:
            if d ["agentID"] == agentID: #am trying

                # decrypt task description
                ct_desc = bytes.fromhex(d["task description"]["ciphertext"])
                nonce1 = bytes.fromhex(d["task description"]["nonce"])
                cipher1 = AES.new(key, AES.MODE_CTR, nonce=nonce1)
                task_desc = cipher1.decrypt(ct_desc).decode('utf-8')

                # decrypt project level
                ct_proj = bytes.fromhex(d["project level"]["ciphertext"])
                nonce2 = bytes.fromhex(d["project level"]["nonce"])
                cipher2 = AES.new(key, AES.MODE_CTR, nonce=nonce2)
                proj_level = cipher2.decrypt(ct_proj).decode('utf-8')

                print(f"Task: {task_desc} | Due: {d['due date']} | Level: {proj_level}")
                # print(f"Task: {d['task description']} | Due: {d['due date']} | level: {d['project level']}")





def display_main_menu():
    print("\n--- MAIN MENU ---")
    print("PRESS 1. REGISTER")
    print("PRESS 2. LOGIN")
    print("PRESS 3. EXIT")
    options = int(input("ENTER OPTION: "))
    return options


def display_registration():
    print("\n--- REGISTER AGENT ---")
    name = input("ENTER NAME: ")
    password = getpass("ENTER PASSWORD: ")



    for user in data["users"]:
        if user["name"] == name:
            print("\nREGISTRATION FAILED. ACCOUNT ALREADY EXISTS\n")
            return

    User.register(name, password)
    print("\nREGISTRATION SUCCESSFUL. WELCOME AGENT\n") 


def display_task_menu():
    print("\n--- TASK MENU ---")
    print("PRESS 1. ADD TASK")
    print("PRESS 2. VIEW TASK")
    print("PRESS 3. LOGOUT")
    choice = int(input("ENTER OPTION: "))
    return choice


# driver function
def main():
    while True:
        options = display_main_menu()
        if options == 1:
            display_registration()
        elif options == 2:
            logged_in = User.login() #b8
            if logged_in:  # only show task menu if login succeeded #b9
                while True:
                    choice = display_task_menu()
                    if choice == 1:
                        t2 = Task("dummy", "none", "none",logged_in.unique_agentID)
                        t2.password = logged_in.password   # attach password for encryption
                        t2.add_task("task.json")
                    elif choice == 2:
                        t3 = Task("dummy", "non","non","non") #only creates a temporary Python object in memory. 
                        t3.password = logged_in.password   # attach password for decryption
                        t3.view_task("task.json",logged_in.unique_agentID) #It does not affect your database (the task.json file) unless you explicitly call add_task or store_task.
                    elif choice == 3:
                        print("LOGGING OUT...")
                        break
                    else:
                        print("INVALID OPTION")
        elif options == 3:
            print("EXITING THE SYSTEM")
            break
        else:
            print("INVALID OPTION")
main()
