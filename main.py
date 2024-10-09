#!/user/bin/python 

def create_task(task=str):
    if len(task) == 0:
        return "Empty task"
    else:
        with open("task", "a") as file:
            file.write(f"{task} \n")
    return "Save task"


task = input("> ")
create_task(task=task)
