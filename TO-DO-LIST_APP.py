###ToDo App
"""This module implements a command-line to-do list application
for efficient task organization.
Author: Samruddhi Tiwari
Date: 05/04/2024
Usage:
Run the script to start the ToDo app. 31
Follow the on-screen instructions to manage your to-do lists and tasks. 12
add Add a new task to the ToDo list
Actions:
add-Add a new task to the list
delete list Delete a task from the Topo list List all tasks in the ToDo list
view-see all tasks
"""
tasks=[]
def add_task():
    """
    add a new task to the to-do list
    """
    task=input("Enter a new Task:")
    tasks.append(task)
    print("Task added Successfully!")





def view_task_list():
    """
    View the tasks in your list
    """
    if len(tasks)==0:
        print("No current tasks.")
    else:
        print("List to tasks:")
        for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')





def delete_task():
    """
    Delete a task from the to-do list
    """
    if len(tasks)==0:
        print("No tasks to delete.")
    else:
        print("Tasks:")
        for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')
        choice=int(input("Enter the task number to delete the task:"))

        if 0<choice<=len(tasks):
            del tasks[choice-1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")




def main():
    """
    Run the To-Do list application.
    """
    while True:
        print("\n******To-Do List Application******")
        print("1.Add Task")
        print("2.View To DOs")
        print("3.Delete Task")
        print("4.Quit Application")

        user_choice=int(input("Enter Your Choice:"))
        if user_choice==1:
            add_task()
        elif user_choice==2:
            view_task_list()
        elif user_choice==3:
            delete_task()
        elif user_choice==4:
            print("Thankyou for using our To-Do List application!")
            break
        else:
            print("Invalid Choice.Please try again.")







if __name__=="__main__":
    main()






