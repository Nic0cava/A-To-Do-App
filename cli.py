# To-Do App

#importing elements from another file
# from functions import get_todos, write_todos
# or like this, and then adding functions. before the function you want to call (eg. functions.get_todos())
import functions
# importing time and date using built in Python modules
import time


now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", now)

while True: 
    # Get user input and account for user input errors 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]#slices user_action to remove the "add " string input

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # This way of opening the file is much better as it makes sure the file closes even if the code stops running on that block of code


        todos = functions.get_todos()
        # Calls the get_todos() function

        todos.append(todo + '\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

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

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()
            # print("Here is todos existing", todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            #print("Here is how it will be", todos)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue # Runs the while loop again


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            print(number)

            todos = functions.get_todos()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command, try again")

print("Goodbye!")