#!/user/bin/python 

def create_task(task=str):
    if len(task) == 0:
        return "Empty task"
    else:
        with open("pending_tasks", "a") as file:
            file.write(f"{task} \n")
    return "Save task"

def view_task():
    with open("pending_tasks", "r") as file:
        count = 1
        for linea in file:
            print(f"[{count}] {linea.strip()}")
            count = count + 1 

#task = input("> ")
#create_task(task=task)

view_task()