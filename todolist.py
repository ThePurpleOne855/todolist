task_list = []
def delete_task():
    print('Tasks:')
    for index, value in enumerate(task_list, start = 1):
        print(f'{index}: {value}')
        
    user_input = int(input('Please provide the enumeration of the task you want to delete: '))
    
    del task_list[user_input]
    
    
        
def create_task():
    task_add = input('New Task: ')
    task_list.append(task_add)
    
    question = input('Would you like to add more?')
    if question == 'yes':
        create_task()
    
        
    
def see_tasks():
    print('These are your current tasks: ')
    for i in task_list:
        print(i)
    
    
while user_input != 4:
    print("""What would you like to do?
                1. Create a task.
                2. See task
                3. Delete task
                4. Finish""")
    
    user_input = input('Action: ')
    if user_input == "1":
        create_task() 
    elif user_input == "2":
        see_tasks()
    elif user_input == "3":
        delete_task()
    else: 
        print('NoValidInput')