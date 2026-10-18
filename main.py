from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_tasks
import os

load_tasks()

name = input("enter your name : ")
print("welcome", name)

admin_mode = input("do you want to enter admin mode?")
if admin_mode == "yes":
    password = input("enter admin password : ")
    if password == "1234":
        print("admine mode activated!")
    else :
        print("wrong password!")

tasks = load_tasks()
count = int(input("how many tasks do you want to add? : "))
for i in range(count):
    task = input("enter a task : ")
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)