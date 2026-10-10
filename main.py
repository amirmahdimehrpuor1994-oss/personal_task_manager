name = input("what's your name ? ")

print("welcome")

task = input("please enter the Task : ")
print(task)

while open("results.txt", "a") in name:
    task.write(f"{name} - {task}")