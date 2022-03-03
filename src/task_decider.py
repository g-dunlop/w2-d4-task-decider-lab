from src.task import Task

# def get_preferred_option(task1, task2):
#     if task2.description in task1.preferred_over:
#         return task1
#     else:
#         return task2


def get_preferred_option(task1, task2):
    if task1.description == "Cook Dinner":
        if task2.description == "Clean Windows" or task2.description == "Do Ironing":
            return task1
        else: 
            return task2
    elif task1.description == "Clean Windows":
        if task2.description == "Wash Dishes" or task2.description == "Do Ironing":
            return task1
        else:
            return task2
    elif task1.description == "Wash Dishes":
        if task2.description == "Cook Dinner" or task2.description == "Wash Clothes":
            return task1
        else:
            return task2
    elif task1.description == "Do Ironing":
        if task2.description == "Wash Clothes" or task2.description == "Wash Dishes":
            return task1
        else:
            return task2
    elif task1.description == "Wash Clothes":
        if task2.description == "Cook Dinner" or task2.description == "Clean Windows":
            return task1
        else:
            return task2
    
