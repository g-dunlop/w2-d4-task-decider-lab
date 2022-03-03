from src.task import Task

def get_preferred_option(task1, task2):
    if task2.description in task1.preferred_over:
        return task1
    else:
        return task2


# def get_preferred_option(task1, task2):
#     if task1.description == "Cook Dinner" and task2.description == "Clean Windows":
#         return task1
#     elif task1.description == "Clean Windows" and task2.description == "Wash Dishes":
#         return task1
#     elif task1.description == "Wash Dishes" and task2.description == "Cook Dinner":
#         return task1
#     else:
#         return task2
    
