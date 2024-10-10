#!/user/bin/python 


filename = "pending_tasks"

def create_task(task=str):
    if len(task) == 0:
        print ("Empty task")
    else:
        with open(filename,"a") as file:
            file.write(f"{task} \n")
    print("Save task")

def view_task():
    try:
        with open(filename, "r") as file:
            count = 0
            for linea in file:
                print(f"[{count}] {linea.strip()}")
                count = count + 1 
    except FileExistsError:
        print("Empty list: no tasks have been created!")

def delete_task(id = int):
    try:
        with open(filename, "r") as file:
            contenido = file.readlines()
            if 0<=id < len(contenido):
                del contenido[id]
                print("Task completed")
            else:
                print("Id Error: id not identified (try running view command to see pending tasks)")

        with open(filename, "w") as file:
            file.writelines(contenido)
            file.close()
    except FileExistsError:
        print("Empty list: no tasks have been created!")


task = int(input("> "))
complite_task(id=task)
#create_task(task=task)
#view_task()