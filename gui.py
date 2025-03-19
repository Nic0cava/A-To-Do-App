import FreeSimpleGUI.window
import functions
import time
import os

# will create the todo.txt file if it doesn't already exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


# third party modules/libraries 
# go to pypi.org to find
# will be using freesimplegui 
import FreeSimpleGUI as sg

# change theme of program, do google search "pysimplegui themes" images
sg.theme("DarkPurple7")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
         [label],
         [input_box, add_button],
         [list_box, edit_button, complete_button],
         [exit_button]]

window = sg.Window("My To-Do App", 
                   layout=layout, 
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200) # displays objects in the layout list
    window["clock"].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo =  values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED: # when x close button is pressed on window
            break
            
print("Bye")
window.close() # closes