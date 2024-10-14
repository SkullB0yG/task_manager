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



#task = input("> ")
#create_task(task=task)
#complete_task(task_complete=task)    
#delete_task(id=task)
view_task()