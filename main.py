# To-Do App



while True: 
    # Get user input and account for user input errors 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if 'add'in user_action:
        todo = user_action[4:] #slices user_action to remove the "add " string input

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # This way of opening the file is much better as it makes sure the file closes even if the code stops running on that block of code
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        #list comprehension of the for loop above
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # print("Here is todos existing", todos)

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        #print("Here is how it will be", todos)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        print(number)

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # print("Here is todos existing", todos)

        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo '{todo_to_remove}' was removed from the list."
        print(message)
        
    elif 'exit' in user_action:
        break
    else:
        print("Invalid command, try again")

print("Goodbye!")