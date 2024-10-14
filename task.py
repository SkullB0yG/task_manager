#!/user/bin/python 

import os

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
            print("[ID  TAKS]")
            for linea in file:
                print(f" {count}   {linea.strip()}")
                count = count + 1 
            file.close()
    except FileExistsError:
        print("Empty list: no tasks have been created!")

def delete_task(id = int):
    try:
        with open(filename, "r") as file:
            contenido = file.readlines()
            if 0<=id < len(contenido):
                del contenido[id]
                print("Task delete")
            else:
                print("Id Error: id not identified (try running view command to see pending tasks)")

        with open(filename, "w") as file:
            file.writelines(contenido)
            file.close()
    except FileExistsError:
        print("Empty list: no tasks have been created!")


def complete_task(task_complete = str):
    try:
        with open(filename, "r") as file:
            contenido = file.readlines()
            loops = 0
            for id, element in enumerate(contenido):

                if task_complete in element and  not "COMPLETE" in element:
                    contenido[id] = element.strip() + " " + " COMPLETE" + "\n"
        
                    with open(filename, "w") as file:
                        file.writelines(contenido)
                        file.close() 
                    print("Task marked as complete") 
                    break

                if task_complete in element and "COMPLETE" in element:
                    print("The task is now complete")
                    break
                
                loops += 1

                if loops == len(contenido):
                    print("Task not Found Error: (try running view command to see pending tasks)")
    except FileExistsError:
        print("Empty list: no tasks have been created!")

def help(): 
    print("""
          comand    info
        1. clear    **clean the console** 
        2. view     **show the tasks**
        3. delete   **delete a task receives the task id as argument**
        4. complete **Marks a task as complete or finished, receiving as argument the task you already finished**
        5. create   **creates a task, receiving as argument the new task you want to add**
    """)

while True:

    try: 
        commant = input("> ")
        commant.lower()
        order_commant = commant.split()

        if order_commant[0] == "view":
            view_task()
        elif order_commant[0] == "create":
            create_task(order_commant[1])
        elif order_commant[0] == "delete":
            id = int(order_commant[1])
            delete_task(id=id)
        elif order_commant[0] == "complete":
            complete_task(order_commant[1])
        elif order_commant[0] =="clear":
            os.system("clear")
        elif order_commant[0] == "quit":
            break
        elif order_commant[0] == "--help":
            help()
        else:
            print("command not found Error")
    except IndexError:
        print("Enter a command try --help to see available commands")
        continue
    except KeyboardInterrupt:
        print(" Exit \n")
        break