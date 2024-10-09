#!/user/bin/python 
import pickle

list_task=[]

def create_task(task=str):
    if len(task) == 0:
        return "empty task"
    else:
        list_task.append(task)
        return "ok"


task = input("> ")

print(create_task(task=task))