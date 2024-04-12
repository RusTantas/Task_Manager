tasks = []
def create_task_list():
    while True:
        task = input("enter task: ")
        if task == "":
            break
        tasks.append(task)
    with open("tasks.txt", "a") as file:
        for task in tasks:
            file.write(task + "\n")

def view_task_list():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())

def mark_task_done():
    tasks = []
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    print("Your task list:")
    for i, task in enumerate(tasks):
        print(f"{i+1}.{task.strip()}")
    task_num = int(input("Enter task number: "))
    tasks[task_num-1] = (tasks[task_num-1].strip() + " done\n")
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task)

def delete_task():
    tasks = []
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    print("Your task list:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}.{task.strip()}")
    task_num = int(input("Enter task number to delete "))
    del tasks[task_num-1]
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task)


# create_task_list()
# mark_task_done()
# view_task_list()
# delete_task()
# view_task_list()

while True:
    print("Choose action")
    print("1. Add task")
    print("2 Delite task")
    print("3 View task")
    print("4 Mark task done")
    print("5. Exite")

    choice = int(input("Enter aktion"))
    if choice == 1:
        create_task_list()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        view_task_list()
    elif choice == 4:
        mark_task_done()
    elif choice ==5:
        break
    else:
        print("Incorrect enter")


