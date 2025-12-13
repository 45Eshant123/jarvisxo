# jarvisxo_laptop_agent.py
# Laptop Agent Starter – Week 2

import os
import subprocess

# ---------------------------
# 1. Open Application Function
# ---------------------------
def open_vs_code():
    try:
        # Windows example
        subprocess.Popen([r"C:\Users\iases\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
        print("JarvisXo: VS Code opened successfully.")
    except Exception as e:
        print(f"JarvisXo: Failed to open VS Code. Error: {e}")

# ---------------------------
# 2. Open Project Folder
# ---------------------------
def open_project(folder_path):
    try:
        # Windows example
        os.startfile(folder_path)
        print(f"JarvisXo: Project '{folder_path}' opened successfully.")
    except Exception as e:
        print(f"JarvisXo: Failed to open project. Error: {e}")

# ---------------------------
# 3. Run Terminal Command
# ---------------------------
def run_terminal_command(command):
    try:
        # For Windows CMD
        subprocess.run(command, shell=True)
        print(f"JarvisXo: Terminal command '{command}' executed.")
    except Exception as e:
        print(f"JarvisXo: Failed to execute command. Error: {e}")

# ---------------------------
# 4. Main Loop for Testing
# ---------------------------
def main():
    print("JarvisXo Laptop Agent Online.\n")
    while True:
        cmd = input("You: ").lower()
        if cmd == "exit":
            print("JarvisXo: Laptop agent shutting down...")
            break
        elif "open vs code" in cmd:
            open_vs_code()
        elif "open project" in cmd:
            folder = input("JarvisXo: Enter project folder path: ")
            open_project(folder)
        else:
            run_terminal_command(cmd)

if __name__ == "__main__":
    main()
