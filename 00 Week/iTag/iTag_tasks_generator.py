from asyncio import current_task
import random

def task_list_import(file_name):
    with open(file_name) as f:
        tasks = f.read().splitlines() 
    return tasks

def task_selector(tasks):
    """Shuffles a task list, which is ready for distributing."""
    tasks_number = len(tasks)
    shuffled_task_list = []
    while tasks_number > 1:
        random_task = random.randrange(0, tasks_number)
        shuffled_task_list.append(tasks[random_task])
        tasks.pop(random_task)
        tasks_number = len(tasks)
    shuffled_task_list.append(tasks[0])
    return shuffled_task_list

def select_tasks(shuffled_task_list, number_of_tasks):
    current_task = []
    while number_of_tasks >= 1:
        current_task.append(shuffled_task_list[number_of_tasks])
        shuffled_task_list.pop(number_of_tasks)
        number_of_tasks = number_of_tasks - 1
    return shuffled_task_list, current_task

def main():
    print("\n")
    tasks = task_list_import(r"D:\Documents\Python\00 Week\iTag\tasklist.txt")
    shuffled_task_list = task_selector(tasks)
    shuffled_task_list, current_task = select_tasks(shuffled_task_list, 5)
    print(current_task)
    tasks_remaining = len(shuffled_task_list)
    while tasks_remaining > 1:
        more = input('\nWould you like another task? (Y/N) ').upper().strip(" .,/qwertuiop[]asdfghjklzxcvbmn?")
        if more == "Y":
            print("\n")
            shuffled_task_list = select_tasks(shuffled_task_list, 1)
            tasks_remaining = len(shuffled_task_list)
        else:
            tasks_remaining = 0
    pass
