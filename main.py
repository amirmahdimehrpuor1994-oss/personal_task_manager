import os
from dotenv import load_dotenv
from tasks import tasks

load_dotenv()
admin_password = os.getenv("QUIZ_ADMIN_PASSWORD")

name = input("what's your name ? ")

print("welcome")

task = input("please enter the Task : ")
print(task)

while open("results.txt", "a") in name:
    task.write(f"{name} - {task}")

    Admin = input("Do you love go to the Admin Mode? (Yes / No)")

    if Admin == "Yes":
        input("please enter the password!")
    elif Admin == "No":
        print("you don't love admin mode!")