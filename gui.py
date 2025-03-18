import FreeSimpleGUI.window
import functions

# third party modules/libraries 
# go to pypi.org to find
# will be using freesimplegui 
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read() # displays objects in the layout list
window.close() # closes